# CSGO-Skinchanger

An external skinchanger for the original Counter-Strike: Global Offensive, started in 2021 as
an early Python project. It runs as a separate process, reads the weapons in your inventory
out of the game's memory and writes the skin IDs you configured in `skins.txt` over them.

It targets the original CS:GO (`csgo.exe`) and has not been adapted to Counter-Strike 2.

## Known limitations

The skinchanger does not apply skins reliably. The cause appears
to be in how an external process and the game interact, a consistent skinchanger would most
likely have to run internally.



## Usage

1. Clone the repository, or download `Skinchanger.py`, `requirements.txt` and `skins.txt`.
2. Install the dependencies once:
   ```
   pip install -r requirements.txt
   ```
3. Edit `skins.txt` to your liking. The skin IDs are listed at https://totalcsgo.com/skin-ids
4. Run `Skinchanger.py`.
