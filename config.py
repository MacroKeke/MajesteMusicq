import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("BABlpKVAqFD0KiiPVVtBZ2g6ZNg8tYOuDkocAeowjzMH4V19HNrSlSWI_ETAPBiZyz-Qtebu4Jj0ncSTo1aQCf3IR-yZGFkBEzOOS91Nz0QuQ5ofOabGgq3N_LtVtLpBu4B0xvjxvsorNpdanAIvJKO2aVqICmzpU9_wY4Xo5zTkwBx9s_c8w-Q2ce9-U5bfcMcM6AxG_mSeOImI2Jqa5PokFwAajKQgf6bbQaiHtfe65NoiJeViW9ymCNb4Y2GXqmRoRfN4uXpRtZWQ1Wb86KwBZ6rHdahVMXjXqiq3tZ7j3Eb7f-SJw5PKQTTkEXwPuK8bpRTrmfsalLNUQG2A9wQkdIRuvgA", "session")
BOT_TOKEN = getenv("213794e62139e26219a5896f5adc8124")
BOT_NAME = getenv("MajesteMusicProBot")
API_ID = int(getenv("13390368"))
API_HASH = getenv("213794e62139e26219a5896f5adc8124")
MONGODB_URL = getenv("mongodb+srv://matesamusic:matesamusic@cluster0.gvs02.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_NAME = getenv("MajesteSahip")
ALIVE_NAME = getenv("Majeste Team")
BOT_USERNAME = getenv("MajesteMusicProBot")
ASSISTANT_NAME = getenv("MajesteMusicAsistan2")
GROUP_SUPPORT = getenv("Majesteler", "Majeste_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MajesteBotlar")
SUDO_USERS = list(map(int, getenv("5077397380").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/189fe27bff1207dd3eb85.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph//file/928cdf4eb56c64b76cc67.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph//file/193c6843e05cfbc35a66a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph//file/31308c6d73cc109c298aa.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph//file/0b2dd8366589068b2c656.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph//file/f9467f8dabec46f589816.jpg")
