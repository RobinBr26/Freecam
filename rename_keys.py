import os
import glob

lang_dir = r"e:\pluginbuild\Freecam-MCPVP-BYPASS\Freecam\common\src\main\resources\assets\freecam\lang\*.json"
files = glob.glob(lang_dir)

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # We want to replace freecam in translation KEYS, not in values.
    # The safest way is direct string replacement of specific anchor patterns.
    content = content.replace('"freecam.', '"fcam.')
    content = content.replace('.freecam.', '.fcam.')
    content = content.replace('"freecam":', '"fcam":')

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print(f"Updated {len(files)} files.")
