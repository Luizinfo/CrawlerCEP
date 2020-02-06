import logs

if __name__ == "__main__":
    pass

def GetCeps():
    try:

        ##Mock list or get from db
        listCeps = ['23575210','23510600']

        return listCeps

    except Error as e:
        logs.Log(f"Error getting ceps - {e}")
    finally:
        logs.Log("Finally GetCeps()")
