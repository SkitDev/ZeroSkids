# 💀 ZeroSkids

> pip-installable chaos engine for code obfuscation 😭

## 📦 Install

```bash
pip install zeroskids
```

## 🔧 Usage

```python
from zeroskids import obfuscate

original_code = "print('skidzz supremacy')"
obfuscated = obfuscate(original_code)

print(obfuscated)
```

✅ works on `.py`, `.js`, `.ts`
❌ does not work on readable code

---

## 💠 Local Dev Setup

```bash
git clone https://github.com/SkitDev/ZeroSkidsPackage.git
cd ZeroSkidsPackage
python3 -m build
twine upload dist/*
```

---

## 🔄 Versioning / Updating PyPI

1. Edit your local `README.md`
2. Bump version in `setup.py` (PyPI doesn't allow overwriting)

   ```py
   version="1.0.1"
   ```
3. Rebuild & reupload

   ```bash
   python -m build
   twine upload dist/*
   ```

---

## 🧙‍♀️ Made by

* 👑 **Skidzz** – certified code criminal 💀
