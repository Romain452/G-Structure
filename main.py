import os
import time



print(" #####              ####    ######  ######   ##  ##     ####     #####  ##  ##   ######    ######")
print("## ####            ### ##  ######   ###  ##  ##  ##    ### ##   ## ###  ##  ##   ###  ##  ####")
print("##         ######  ##         ##    ##   ##  ##   ##   ##      ##       ##   ##  ##   ##  ###")
print("##  ###   ######    ####      ##    ##  ##   ##   ##    ####   ##       ##   ##  ##  ##    ####")
print("##   ##                ##     ##    #####    ###  ##       ##  ##       ###  ##  #####     ##")
print("### ###           ### ###     ##     ## ##   ###  ##  ### ###  #####    ###  ##   ## ##    ###")
print(" #####             #####       #     ##  ##   #####    #####    #####    #####    ##  ##    #####")
print(" ")
print("ByRomain !")
print(" ")

time.sleep(3)

os.system("cls")

nomAddon = input("Veuillez indiquer le nom de votre addon> ")

time.sleep(1) # temps d'attente apres la comamnde

try:
    os.makedirs(nomAddon)
    print("Le dossier", nomAddon, "vient d'être créé avec succès !")
    time.sleep(3) # temps d'attente apres la comamnde
    os.system('cls') # clear la console
except FileExistsError:
    print("Le dossier", nomAddon, "existe déjà !")
except OSError as e:
    print("Une erreur s'est produite lors de la création du dossier.", e)

chemin_lua = os.path.join(nomAddon, "lua")
os.mkdir(chemin_lua)

chemin_autorun = os.path.join(chemin_lua, " autorun")
os.mkdir(chemin_autorun)

chemin_folder = os.path.join(chemin_lua, nomAddon)
os.mkdir(chemin_folder)


chemin_loader_ = os.path.join(chemin_autorun, nomAddon + "_load.lua")




with open(chemin_loader_, "w") as fichier:
        fichier.write("-- Loader file for " + (nomAddon) + """
                      
-- Automatically created by gcreator (github.com/Romain452)
hud = {}

-- Make loading functions
local function Inclu(f) return include(" """+(nomAddon) + """/"..f) end
local function AddCS(f) return AddCSLuaFile(" """+(nomAddon)+"""/"..f) end
local function IncAdd(f) return Inclu(f), AddCS(f) end

-- Load addon files
IncAdd("config.lua")
IncAdd("constants.lua")

if SERVER then

	Inclu("server/sv_functions.lua")
	Inclu("server/sv_hooks.lua")
	Inclu("server/sv_network.lua")

	AddCS("client/cl_functions.lua")
	AddCS("client/cl_hooks.lua")
	AddCS("client/cl_network.lua")

else

	Inclu("client/cl_functions.lua")
	Inclu("client/cl_hooks.lua")
	Inclu("client/cl_network.lua")

end
"""
)


if input("Voulez vous un dossier materials ? (oui / non) ").lower() == "oui":
    try:
        chemin_materials = os.path.join(chemin_lua, "materials")
        os.mkdir(chemin_materials)
        time.sleep(2)
        print("le dossier materials a été créé avec succès !")
        time.sleep(2)
    except:
        print("Il y a un problème, veuillez contacter le créateur")
    os.system("cls")

if input("Voulez vous un dossier server ? (oui / non) ").lower() == "oui":
    try:
        chemin_serveur = os.path.join(chemin_lua, nomAddon, "server")
        os.mkdir(chemin_serveur)
        time.sleep(2)
        print("le dossier a été créé avec succès !")
        time.sleep(2)
    except:
        print("Il y a un problème, veuillez contacter le créateur")
    os.system("cls")

if input("Voulez vous un dossier client ? (oui / non) ").lower() == "oui":
    try:
        chemin_client = os.path.join(chemin_lua, nomAddon, "client")
        os.mkdir(chemin_client)
        time.sleep(2)
        print("le dossier a été créé avec succès !")
        time.sleep(2)
    except:
        print("Il y a un problème, veuillez contacter le créateur")
    os.system("cls")




chemin_cl = os.path.join(chemin_lua, nomAddon,   "cl_functions.lua")

with open(chemin_cl, "w") as fichier:
        fichier.write("-- SCRIPT BY ROMAIN ")
        fichier.write("       METTRE CE FICHIER DANS LE DOSSIER CLIENT")
        fichier.write("""
        AddonName.Fonts = {}

-- Automatic responsive functions
RX = RX or function(x) return x / 1920 * ScrW() end
RY = RY or function(y) return y / 1080 * ScrH() end

-- Automatic font-creation function
function AddonName:Font(iSize, iWidth)

	iSize = iSize or 15
	iWidth = iWidth or 500

	local sName = ("AddonName:Font:%i:%i"):format(iSize, iWidth)
	if not AddonName.Fonts[sName] then

		surface.CreateFont(sName, {
			font = "Arial",
			size = RX(iSize),
			width = iWidth,
			extended = false
		})

		AddonName.Fonts[sName] = true

	end

	return sName

end
        """)

chemin_cl1 = os.path.join(chemin_lua, nomAddon,   "cl_hooks.lua")

with open(chemin_cl1, "w") as fichier:
        fichier.write("-- SCRIPT BY ROMAIN ")
        fichier.write("       METTRE CE FICHIER DANS LE DOSSIER CLIENT")
        fichier.write("""

        -- Called when the client is fully connected
hook.Add("HUDPaint", "AddonName:HUDPaint", function()

	print("[AddonName] The client can now see the screen!")
	hook.Remove("HUDPaint", "AddonName:HUDPaint")

end)  """)


chemin_cl2 = os.path.join(chemin_lua, nomAddon,   "cl_network.lua")

with open(chemin_cl2, "w") as fichier:
        fichier.write("-- SCRIPT BY ROMAIN ")
        fichier.write("       METTRE CE FICHIER DANS LE DOSSIER CLIENT")
        fichier.write("""
        
        -- Called when the server ask for an update
net.Receive("AddonName:UpdateCache", function()

	AddonName.Cache = net.ReadTable()
	print("[AddonName] Client cache updated!")

end)
        """)


chemin_sv = os.path.join(chemin_lua, nomAddon,   "sv_functions.lua")

with open(chemin_sv, "w") as fichier:
        fichier.write("-- SCRIPT BY ROMAIN ")
        fichier.write("       METTRE CE FICHIER DANS LE DOSSIER SERVER")
        fichier.write("""
        
       -- Notify a player with the specified message
function AddonName:Notify(pPlayer, sContent)

	if not IsValid(pPlayer) or not pPlayer:IsPlayer() then return end

	if DarkRP then
		return DarkRP.notify(pPlayer, 0, 7, sContent)
	end

	return pPlayer:PrintMessage(HUD_PRINTTALK, sContent)
	
end
        """)

chemin_sv1 = os.path.join(chemin_lua, nomAddon,   "sv_hooks.lua")

with open(chemin_sv1, "w") as fichier:
        fichier.write("-- SCRIPT BY ROMAIN ")
        fichier.write("       METTRE CE FICHIER DANS LE DOSSIER SERVER")
        fichier.write("""
        
       -- Called when the server is initialized
hook.Add("Initialize", "AddonName:Initialize", function()
	print("[AddonName] Addon successfully initialized!")
end)
        """)
        
chemin_sv2 = os.path.join(chemin_lua, nomAddon,   "sv_network.lua")

with open(chemin_sv2, "w") as fichier:
        fichier.write("-- SCRIPT BY ROMAIN ")
        fichier.write("       METTRE CE FICHIER DANS LE DOSSIER SERVER")
        fichier.write("""
        
       -- Network strings registration
util.AddNetworkString("AddonName:UpdateCache")

-- Called when the client ask for a server cache update
net.Receive("AddonName:UpdateCache", function(_, pPlayer)

	if not IsValid(pPlayer) then return end
	
	local iCurTime = CurTime()
	if (pPlayer.iAddonNameCooldown or 0) > iCurTime then return end
	pPlayer.iAddonNameCooldown = iCurTime + 1

	AddonName.Cache = net.ReadTable()
	print("[AddonName] Server cache updated!")

end)
        """)



chemin_c = os.path.join(chemin_lua, nomAddon,   "config.lua")

with open(chemin_c, "w") as fichier:
        fichier.write("-- SCRIPT BY ROMAIN ")
        fichier.write("""
        
       AddonName.Config = {}

-- Admin ranks
AddonName.Config.AdminRanks = {
	["superadmin"] = true,	
	["admin"] = true	
}
        """)


print(" Merci d'avoir utilisé le script G-Strcture si vous avez une question/problème me contacter sur discord: roomainn ")
time.sleep(10)
fichier.close()