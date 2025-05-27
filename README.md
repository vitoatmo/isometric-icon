# ISOMETRIC ICON

A simple library of isometric PNG icons for animals, objects, and personas. Metadata for each icon is provided in JSON files for easy mapping and integration.

## Folder Structure

```
01_animals/      # Animal icons (.png)
02_things/       # Object icons (.png)
03_persona/      # Persona icons (.png)
data/            # JSON metadata (e.g., animals.json)
python/          # Utility scripts (.py)
```

## How to Use

* Copy the folders you need (e.g. `01_animals/` and `data/animals.json`) into your project.
* Use the metadata JSON file to match filenames to icon names, tags, and descriptions.

## Example

* Icon: `01_animals/lion.png`
* Metadata: `data/animals.json`

  ```json
  [
    {
      "filename": "lion.png",
      "slug": "lion",
      "name": "Lion",
      "tags": ["animals", "mammal", "wild"],
      "desc": "A large, social big cat known as the 'king of the jungle.'"
    }
  ]
  ```

## Scripts

Python scripts in the `python/` folder can help you:

* Rename images to a consistent format
* Generate or update metadata JSON files from CSV

Run scripts with:

```
python3 python/script_name.py
```

---

Simple. Modular. Ready to use in any project.
