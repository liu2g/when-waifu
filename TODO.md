# TODO

As far as now, this file describes how this application behaves on the top level.
With the preliminary concept described below, there are some decisions to finalize as well as some implementations to attempt. 

## TBD Concepts

### Architecture
The projected architecture is pictured in the flowchart below.
The UI will be implemented mainly for terminal/command use, where users manage their list of channels with simple commands such as `sub`, `unsub`, `print` etc.
Then the UI util writes/updates the user settings with a local config file, where the scraper reads out of to fetch stream data.

```
             ┌-------------┐
     ┌-----> | config-file | <-┐
read |       └-------------┘   | write
     |                         |
┌---------┐     request     ┌----┐
| scraper | <-------------- | UI |
└---------┘                 └----┘
```

### UI Command List
- `when-waifu <config-file>` to print stream list from the favorites, if no config file is used, use a default one.
- `when-waifu sub/unsub <channel>` add/remove channels to the default config file.
Should support both indivisual channel, groups of channels by fuzzy search (good to have feature).
- `when-waifu check <config-file>` check the format of the config file, and prettily print configs.
- `when-waifu config <key> <value>` to change individual settings other than the channel list.

## Tasks to try
- [ ] Web scraper implementation

## Decisions to determine
- [ ] Config file format
- [ ] UI command list and expected behavior


