# Crowdin Translation Platform Integration

## Requirements

1. git
2. svn
3. python
4. gettext-tools
5. crowdin-cli (version 2)

You also need a API key given by project maintainers. Create a file at `~/.crowdin.yaml`:

```yaml
"api_key" : "<your_key_string>"
```

## Initialize

```sh
git clone https://github.com/KDE-China/crowdin.git
cd crowdin
./init
```

## Synchronization

```sh
./sync
```
