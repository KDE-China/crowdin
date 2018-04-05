# Crowdin 翻译同步工作流

## 系统需求

1.  git
2.  svn
3.  python
4.  gettext-tools
5.  crowdin-cli (version 2)

You also need a API key given by project maintainers. Create a file at `~/.crowdin.yaml`:

```yaml
"api_key" : "<your_key_string>"
```

## 初始化

```sh
git clone https://github.com/KDE-China/crowdin.git
cd crowdin
./init
```

## 同步

```sh
./sync
```

## 添加新语言

比如要添加中文（香港）。

首先在 Crowdin 网站上的设置里，添加新的 Target Language 。

然后需要修改 init 脚本，在 $LANGS 里添加 zh_HK 。注意这里连字符是 \_ 。然后运行

```
./init
```

再后需要更改 commit, backup_credits 和 resotre_credits 脚本中的 $LANGS 变量。

最后运行翻译上传脚本：

```
./upload_translations zh-HK
```

注意语言代码里的连字符是 - 。

以后的同步流程不变。

## 常见问题解答

### Crowdin 上传/下载进度卡住

**没办法，重新跑吧**。我们的文件太多又大，如果网络不好断了，只能重来。

### SVN 提交被拒绝

**得手动解决，挺累的**。SVN 有检查脚本，如果源字符串和翻译字符串的变量或者换行不匹配，就容易被拒绝。这时你要看报错的是哪个文件哪一行，不止要手动编辑 PO 文件，还要在 Crowdin 上找到对应的字符串改了。这个事情还挺费力的，但是没有别的办法。

### 翻译大量丢失

**翻译存储救命**。有些软件经历一个大版本，导致模板变化，很可能会令翻译渐渐丢失。但是翻译存储里面的是不会丢的。这时候你需要去 Project Settings 然后打开 TM & MT 标签页，点击 Pre-translate 选 via TM 然后选项如下：

![](https://screenshots.firefoxusercontent.com/images/f8cc5931-bb29-4553-bd3a-640342260305.png)

点击 **Pre-Translate** 按钮，可能会花上几个小时才能跑完，你可以关掉窗口等着。几个小时后，你就能在 Activities 里面看到有多少字符串被翻译了。

### 头部贡献者名单

Crowdin 不能更新头部注释内的贡献者名单，而且不能保留旧的注释。我们现在用一个脚本来将头部备份和恢复，但是 Crowdin 上的新翻译者，我们必须得手动添加到注释里面去。

## Crowdin 设置

TODO
