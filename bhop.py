import pymem
import win32api
import time

#offsets
LOCAL_PLAYER = 14316652
FORCE_JUMP = 86422944
HEALTH = 256
FLAGS = 260

def bhop() -> None:
    pm = pymem.Pymem('csgo.exe')

    # get module adress artık csgonun modül listesinden geçerek istemcinin adresini alabiliriz
    for module in list(pm.list_modules()):
        client module.lpBaseofDll

# hack loop bburada sonsuz bir while döngüsü oluşturarak hack döngümüzü oluşturup cpu kullanımından tasarruf etmek için onu uyutabiliriz
while True:
    time.sleep(0.01)

    # space bar win32 apiyi anahtar durumdaki gettylerle birlikte space e basıp basmadığınızı kontrol etmek için yerel oynataıcınızı almak ve geçerli olduğuna emin olmak için pym ın okuma işlemi hafıza işlemlerini kullandık
    if not win32api.GetAsyncKeyState(0x20):
        continue

        local_Player: int = pm.read_uint(client + LOCAL_PLAYER)

        if not local_player:
            continue

            # is alive oyuncunun hayatta olup olmadığından emin olmak için oyuncunun sağlığını öğrendik
            if not pm_read_int(local_player + HEALTH):
                continue

                #on ground yerdeysek istemciye 6 yazan ve kendinizi zıplatan ve 10 milisaniye bekleyen kodu yazdık
                if pm.read_uint(local_Player + FLAGS) & 1 << 0:
                    pm.write_uint(client + FORCE_JUMP, 6)
                    time.sleep(0.01)
                    pm.write_uint(client + FORCE_JUMP, 4)

if __name__ == '__main__':
    bhop()