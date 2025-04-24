import grpc
import grpc_services.alerta_pb2 as alerta_pb2
import grpc_services.alerta_pb2_grpc as alerta_pb2_grpc

def verificar_alerta(dado):
    canal = grpc.insecure_channel('localhost:50051')
    stub = alerta_pb2_grpc.AlertaServiceStub(canal)

    resposta = stub.VerificarTemperatura(alerta_pb2.DadoSensor(
        ambiente=dado['ambiente'],
        temperatura=dado['valor'],
        timestamp=dado['timestamp']
    ))

    return resposta.mensagem
