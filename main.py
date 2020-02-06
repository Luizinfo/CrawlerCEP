import logs
import ceps
from datetime import datetime
import correiosService

def Start():
    now = datetime.now()
    cepsList = ceps.GetCeps()

    for cep in cepsList:
        try:
            ret = f'CEP: {cep} localizado com sucesso!'
            endereco = correiosService.ConsultarCepPage(cep)
            logs.Log(ret)
            logs.Log(endereco.GetObjectText())
        except Exception as e:
            logs.Log(f'Cep: {cep} Erro: {str(e)}')

if __name__ == '__main__':
    try:
        Start()
    except Exception as ex:
        print(f'Erro na execução do serviço -> {ex}')

