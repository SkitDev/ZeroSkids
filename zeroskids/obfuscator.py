import base64
import random
import string

# === PRESETS ===
PRESETS = {
    "light": 1,
    "skidproof": 3,
    "demonic": 10
}

# === JUNK CODE ===
def insert_junk(code: str, amount=3) -> str:
    junk = ""
    for _ in range(amount):
        junk += f"\n{random.choice(['if True:', 'if False:', 'while False:', ''])}\n    {random_var()} = {random.randint(0,999999)}"
    return junk + "\n" + code

# === VAR MANGLE ===
def random_var():
    return "_" + ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def mangle_vars(code: str) -> str:
    var_names = set()
    for word in code.split():
        if word.isidentifier() and not word in dir(__builtins__):
            var_names.add(word)
    mapping = {name: random_var() for name in var_names}
    for k,v in mapping.items():
        code = code.replace(k, v)
    return code

# === LAYERS ===
def hex_layer(code: str) -> str:
    return f"exec(bytes.fromhex('{code.encode().hex()}').decode())"

def base64_layer(code: str) -> str:
    encoded = base64.b64encode(code.encode()).decode()
    return f"import base64\nexec(base64.b64decode('{encoded}').decode())"

# === FINAL OBFUSCATION ===
def obfuscate(code: str, preset: str = "skidproof") -> str:
    layers = PRESETS.get(preset, 3)
    result = code

    result = mangle_vars(result)
    result = insert_junk(result, amount=5)

    for _ in range(layers):
        result = hex_layer(result)

    final = base64_layer(result)
    watermark = "# obfuscated with ZeroSkids v2 💀 try harder skiddy\n"

    return watermark + final

# === ULTRA OBFUSCATION ===
def ultra_obfuscate(code: str) -> str:
    result = code
    for i in range(25):
        if i % 5 == 0:
            result = mangle_vars(result)
        if i % 4 == 0:
            result = insert_junk(result, amount=2)
        if i % 3 == 0:
            result = base64_layer(result)
        else:
            result = hex_layer(result)
    final = base64_layer(result)
    watermark = "# ultra-obfuscated with ZeroSkids v2 💀 25-layer death sauce\n"
    return watermark + final
