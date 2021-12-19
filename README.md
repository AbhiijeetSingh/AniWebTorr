# AniWebTorr

A CLI to integrate the webtorrent-cli and get magnets from nyaa.si using NyaaPy, 
to download and open episodes directly in mpv.

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
