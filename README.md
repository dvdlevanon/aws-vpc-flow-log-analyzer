Simple tool to analyze [AWS vpc flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in its default format that looks like:

```
version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status
```

# Usage

Run `./download_and_analyze.sh`
