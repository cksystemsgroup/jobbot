# JobBot

This small python script uses the Incoming WebHook integration of Slack to post messages.
One possible use case is to announce the completion of a long running job at one of our servers.

## Example

To post a message to the `#servers` channel use the following command

```
$ long-running-command && jobbot "My work is done"
```

This will post the following message:

> Job for user `user` on machine `machine`: _My work is done_
