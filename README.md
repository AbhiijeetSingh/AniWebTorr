# AniWebTorr

A CLI to integrate the webtorrent-cli and get magnets from nyaa.si using [NyaaPy](https://github.com/JuanjoSalvador/NyaaPy), to download and open episodes directly in mpv.

# Prerequisites
Install webtorrent-cli. The process can be found [here](https://github.com/webtorrent/webtorrent-cli).
Make sure that mpv is accessible via the terminal(it is added to the PATH).
After cloning the repository run install all the requirments using
```sh
pip install -r requirements.txt
```

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

You can even use magnet links to play the video. just use

```sh
main.py magnet
```

You can also use SeaSmoke's Index inside the CLI to look for recommendation from the index.
(Using https://github.com/DhanrajHira/seadex_api)

```sh
main.py smokes
```
