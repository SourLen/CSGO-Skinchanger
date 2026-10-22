# CSGO-Skinchanger

An external skinchanger for the original Counter-Strike: Global Offensive, started in 2021 as
an early Python project. It runs as a separate process, reads the weapons in your inventory
out of the game's memory and writes the skin IDs you configured in `skins.txt` over them.

It targets the original CS:GO (`csgo.exe`) and has not been adapted to Counter-Strike 2.

## Known limitations

The skinchanger does not apply skins reliably. The original README put the success rate at
roughly 80% in matchmaking, both for the automatic change and for the manual retry on F6 —
that number comes from informal testing back then, not from a measurement. The cause appears
to be in how an external process and the game interact; a consistent skinchanger would most
likely have to run internally.

Other known issues:

- The skin does not always change.
- If a weapon already has a skin equipped, the skin does not change.

## Usage

1. Clone the repository, or download `Skinchanger.py`, `requirements.txt` and `skins.txt`.
2. Install the dependencies once:
   ```
   pip install -r requirements.txt
   ```
3. Edit `skins.txt` to your liking. The skin IDs are listed at https://totalcsgo.com/skin-ids
4. Run `Skinchanger.py`.
