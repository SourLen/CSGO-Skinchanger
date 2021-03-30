import time
import ctypes
import pymem
import requests
import keyboard

offsets = 'https://raw.githubusercontent.com/naaax123/Python-CSGO-Cheat/main/offsets/offsets.json'
response = requests.get( offsets ).json()

dwClientState = int( response["signatures"]["dwClientState"] )
dwLocalPlayer = int(response['signatures']['dwLocalPlayer'])
m_hMyWeapons = int(response['netvars']['m_hMyWeapons'])
dwEntityList = int(response["signatures"]["dwEntityList"])
m_iItemDefinitionIndex = int(response["netvars"]["m_iItemDefinitionIndex"])
m_OriginalOwnerXuidLow = int(response["netvars"]["m_OriginalOwnerXuidLow"])
m_iItemIDHigh = int(response["netvars"]["m_iItemIDHigh"])
m_nFallbackPaintKit = int(response["netvars"]["m_nFallbackPaintKit"])
m_iAccountID = int(response["netvars"]["m_iAccountID"])
m_nFallbackStatTrak = int(response["netvars"]["m_nFallbackStatTrak"])
m_nFallbackSeed = int(response["netvars"]["m_nFallbackSeed"])
m_flFallbackWear = int(response["netvars"]["m_flFallbackWear"])

user32 = ctypes.windll.user32

pm = pymem.Pymem( "csgo.exe" )
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll

def GetWindowText(handle, length=100):

    window_text = ctypes.create_string_buffer(length)
    user32.GetWindowTextA(
        handle,
        ctypes.byref(window_text),
        length
    )

    return window_text.value.decode('cp1252')


def GetForegroundWindow():

    return user32.GetForegroundWindow()

def change_skin():
    akpaint = 44
    awppaint = 344
    usppaint = 654
    deaglepaint = 962
    glockpaint = 38
    fivepaint = 44
    ppaint = 102
    tecpaint = 179
    mapaint = 309
    mspaint = 445
    galilpaint = 379
    famaspaint = 260
    augpaint = 455
    sgpaint = 287
    scoutpaint = 624
    macpaint = 433
    mpsevpaint = 102
    mpninpaint = 734
    pppaint = 542
    pneunpaint = 359
    umppaint = 37
    magpaint = 737
    novpaint = 537
    sawpaint = 256
    xmpaint = 852
    engine_state = pm.read_int( engine + dwClientState )
    while True:
        if not GetWindowText( GetForegroundWindow() ) == "Counter-Strike: Global Offensive":
            time.sleep( 1 )
            continue
        local_player = pm.read_int( client + dwLocalPlayer )
        if local_player == 0:
            continue
        for i in range( 0, 8 ):
            my_weapons = pm.read_int( local_player + m_hMyWeapons + (i - 1) * 0x4 ) & 0xFFF
            weapon_address = pm.read_int( client + dwEntityList + (my_weapons - 1) * 0x10 )
            if weapon_address:
                weapon_id = pm.read_int( weapon_address + m_iItemDefinitionIndex )
                weapon_owner = pm.read_int( weapon_address + m_OriginalOwnerXuidLow )
                seed = 420
                if weapon_id == 7:
                    fallbackpaint = akpaint
                    seed = 661
                elif weapon_id == 9:
                    fallbackpaint = awppaint
                    seed = 420
                elif weapon_id == 61:
                    fallbackpaint = usppaint
                    seed = 420
                elif weapon_id == 1:
                    fallbackpaint = deaglepaint
                    seed = 420
                elif weapon_id == 4:
                    fallbackpaint = glockpaint
                    seed = 420
                elif weapon_id == 3:
                    fallbackpaint = fivepaint
                    seed = 420
                elif weapon_id == 36:
                    fallbackpaint = ppaint
                    seed = 420
                elif weapon_id == 30:
                    fallbackpaint = tecpaint
                    seed = 420
                elif weapon_id == 16:
                    fallbackpaint = mapaint
                elif weapon_id == 60:
                    fallbackpaint = mspaint
                elif weapon_id == 13:
                    fallbackpaint = galilpaint
                elif weapon_id == 10:
                    fallbackpaint = famaspaint
                elif weapon_id == 262152:
                    fallbackpaint = augpaint
                elif weapon_id == 39:
                    fallbackpaint = sgpaint
                elif weapon_id == 40:
                    fallbackpaint = scoutpaint
                elif weapon_id == 17:
                    fallbackpaint = macpaint
                elif weapon_id == 33:
                    fallbackpaint = mpsevpaint
                elif weapon_id == 34:
                    fallbackpaint = mpninpaint
                elif weapon_id == 26:
                    fallbackpaint = pppaint
                elif weapon_id == 19:
                    fallbackpaint = pneunpaint
                elif weapon_id == 24:
                    fallbackpaint = umppaint
                elif weapon_id == 27:
                    fallbackpaint = magpaint
                elif weapon_id == 35:
                    fallbackpaint = novpaint
                elif weapon_id == 262173:
                    fallbackpaint = sawpaint
                elif weapon_id == 25:
                    fallbackpaint = xmpaint
                else:
                    continue
                pm.write_int( weapon_address + m_iItemIDHigh, -1 )
                pm.write_int( weapon_address + m_nFallbackPaintKit, fallbackpaint )
                pm.write_int( weapon_address + m_iAccountID, weapon_owner )
                pm.write_int( weapon_address + m_nFallbackStatTrak, 187 )
                pm.write_int( weapon_address + m_nFallbackSeed, seed )
                pm.write_float( weapon_address + m_flFallbackWear, float( 0.000001 ) )

        if keyboard.is_pressed( "f6" ):
            pm.write_int( engine_state + 0x174, -1 )

if __name__ == "__main__":
    change_skin()