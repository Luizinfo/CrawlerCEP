from datetime import datetime

if __name__ == "__main__":
    pass

def Log(dados):
    try:
        print(dados)
        now = datetime.now()
        date_time = now.strftime('%Y-%m-%d-%H%M%S')
        f = open("log.txt", "a", encoding='utf-8')
        f.write(date_time + ' - ' + dados + "\n")
        f.close()
    except Exception as e:
        print(f'Erro ao gravar Log. Erro: {str(e)}')