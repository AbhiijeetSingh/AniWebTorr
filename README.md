# AniWebTorr

A CLI to integrate the webtorrent-cli and get magnets from nyaa.si using [NyaaPy](https://github.com/JuanjoSalvador/NyaaPy), 
to download and open episodes directly in mpv.

# Prerequisites
Install webtorrent-cli. The process can be found [here](https://github.com/webtorrent/webtorrent-cli).
Make sure that mpv is accessible via the terminal(it is added to the PATH)

# Usage

```sh
main.py search
```
To search the anime using its name and get a list of result that you can choose from

if the torrent file has more than one file, then webtorrent-cli will prompt you to provide the index of
the file which is to be played.

Or use
```sh
main.py recents
```

And select any recently watched anime from the results
