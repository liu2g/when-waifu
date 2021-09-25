# TODO

As far as now, this file describes how this application behaves on the top level.

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

With the preliminary design, there are some decisions to finalize as well as some implementations to attempt. 

## Tasks to try
- [ ] Web scraper implementation

## Decisions to determine
- [ ] Config file format
- [ ] UI command list and expected behavior

