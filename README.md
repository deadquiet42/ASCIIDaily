# asciidaily

Daily ASCII field. Deterministic per day. 80x28. Date seeded.

## quick start

```
python3 asciidaily.py > today.txt
cat today.txt
```

## cron

Run once a day. Example:

```
# minute hour day month dow command
5 0 * * * /usr/bin/python3 ~/asciidaily/asciidaily.py > ~/public_html/asciidaily.txt
```

## notes

- `makeascii` is the wrapper I use on tilde.town
- edit paths to suit your home dir
