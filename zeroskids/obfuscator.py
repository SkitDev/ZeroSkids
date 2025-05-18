def obfuscate(code: str) -> str:
    return "exec(" + repr("".join([f'\\x{ord(c):02x}' for c in code])) + ")"
