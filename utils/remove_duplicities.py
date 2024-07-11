import sys
import os

def remove_duplicates(input_file):
    try:
        # Načtení souboru
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Zjištění duplicitních řádků
        seen = set()
        duplicates = []
        unique_lines = []
        
        for line in lines:
            if line.strip() == "":
                unique_lines.append(line)
            elif line in seen:
                duplicates.append(line)
            else:
                seen.add(line)
                unique_lines.append(line)
        
        # Vypsání duplicitních řádků
        if duplicates:
            print("Duplicitní řádky:")
            for duplicate in duplicates:
                print(duplicate, end='')
        else:
            print("Žádné duplicitní řádky nebyly nalezeny.")
        
        # Získání adresáře a názvu souboru
        dir_name = os.path.dirname(input_file)
        base_name = os.path.basename(input_file)
        output_file = os.path.join(dir_name, "unique_" + base_name)
        
        # Uložení nového souboru
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(unique_lines)
        
        print(f"Nový soubor bez duplicitních řádků byl uložen jako {output_file}")
    
    except Exception as e:
        print(f"Chyba při zpracování souboru: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Použití: python skript.py <název_souboru>")
    else:
        input_file = sys.argv[1]
        remove_duplicates(input_file)
