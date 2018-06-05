# Crowdin 翻译同步工作流

# 已迁移到 GitLab -> https://gitlab.com/kde-china/crowdin

- [翻译流程（开放参与）](#翻译流程)
- [同步流程（限管理员）](#同步流程)

# 翻译流程

## 加入交流群

开源工作交流是要务。目前有两个主要的交流群：

* 微信 - 没有公开链接，加群主 guoyunhebrave 为好友，然后邀请加入群
* Telegram - [点击加入](https://t.me/kde_cn)

## 注册 Crowdin 账号并加入团队

[项目主页](https://crowdin.com/project/kdeorg)

注册后，加入团队，即可开始翻译。但是在动工之前，请先仔细阅读下面的内容，了解基本的翻译注意事项。

Crowdin 是一个在线翻译协作平台。于 2017 年由 Guo Yunhe 引入。在此之前，只有少数拥有 KDE 提交权限的开发者可以直接翻译，其他人只能发送翻译文件到邮件列表，然后等人审核。Crowdin 带来的便利有以下几点：

* 开放参与。任何人都可以注册账号，加入团队，翻译贡献。每个人的翻译记录都会被记录下来，而不会被覆盖或丢弃。贡献者之间相互审核，选择最优的翻译。已通过的翻译会被 KDE 包含，或者最新的翻译。
* 透明运作。任何操作都会记录在活动日志当中，有不当翻译或者蓄意破坏很容易被发现并撤销。同时管理员的行为也会被监督。
* 翻译存储。不止 KDE 项目的翻译存储，Crowdin 上成千上万开源项目的翻译存储都可以作为参考。使翻译更加便利。
* 机器翻译。虽然机器翻译质量参差不齐，但也是一种有益的参考。
* 分支同步。KDE 有两个主要分支，trunk 和 stable。以前我们要同时翻译两个分支，用 Lokalize 设置起来十分繁琐。而 Crowdin 可以自动将两个分支上对应的文件的翻译同步，无需重复翻译或者进行复杂的设置。
* 操作简单。不需要会使用 Subversion 和 Lokalize 等工具，不需要每次手动在邮件列表投递。

## 使用 Crowdin 操作界面

请参考此链接 https://crowdin.com/page/tour#tab_translators

1. 如果一个字符串没有翻译，则你可以提交新的翻译建议。新的翻译建议虽然尚未审核，但也会同步到 KDE 项目中。
2. 如果一个字符串已有翻译，但尚未审核通过，则新提交的翻译会被优先采用，同步到 KDE 项目中。
3. 如果一个字符串已有翻译，且已经审核通过，则新提交的翻译不会被使用。如果你认为已审核通过的翻译有问题，可以在右侧的评论面板中提出，并选中 **Issue**。管理员和原翻译者都会收到通知，并作出回复。

## 翻译原则

1. 优先级。软件优先，文档次要。在文件树里 kf5-trunk/messages 和 kf5-stable/messages 是最重要的，而 docmessages 则是很次要的，很少有用户去看。文件夹按照重要程度进行了排序，排在前面的优先翻译。
2. 谨慎使用翻译存储和机器翻译。翻译存储并不都是正确的，有的错误非常明显。机器翻译大部分时候也不能直接使用。翻译者需要仔细检查，适当修改。
3. 批量替换某个词汇/术语的翻译之前，最好和其它人商量一下。

## 一般规范

# 同步流程

源字符串流向: SVN --> Local --> Crowdin

翻译字符串流向: Crowdin --> Local --> SVN

## 系统需求

1.  git
2.  svn
3.  python
4.  gettext-tools
5.  crowdin-cli (version 2)

You also need an API key given by project maintainers. Create a file at `~/.crowdin.yaml`:

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

然后需要修改 [environment](environment) 脚本，在 $LANGS 里添加 zh_HK 。注意这里连字符是 \_ 。然后运行

```
./init
```

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
