import grpc
from concurrent import futures
import time

import grpc_services.alerta_pb2 as alerta_pb2
import grpc_services.alerta_pb2_grpc as alerta_pb2_grpc

class AlertaService(alerta_pb2_grpc.AlertaServiceServicer):
    def VerificarTemperatura(self, request, context):
        if request.temperatura > 28.0:
            return alerta_pb2.RespostaAlerta(
                alerta=True,
                mensagem=f"ALERTA! Temperatura alta em {request.ambiente} ({request.temperatura}°C)"
            )
        else:
            return alerta_pb2.RespostaAlerta(
                alerta=False,
                mensagem=f"Temperatura normal em {request.ambiente} ({request.temperatura}°C)"
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    alerta_pb2_grpc.add_AlertaServiceServicer_to_server(AlertaService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC rodando na porta 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
