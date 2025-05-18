import base64

def obfuscate(code: str) -> str:
    # First layer: base-level exec(hex)
    def hex_layer(c: str) -> str:
        return f"exec(bytes.fromhex('{c.encode().hex()}').decode())"

    # Layer 1
    result = code
    for _ in range(10):
        result = hex_layer(result)

    # Final deep obfuscation w/ base64
    encoded = base64.b64encode(result.encode()).decode()
    watermark = "# ts script has been obfuscated 11 times w/ 'ZeroSkids' 😭💀 skid-proof.\n"

    final_payload = f"import base64;exec(base64.b64decode('{encoded}').decode())"
    return watermark + final_payload
