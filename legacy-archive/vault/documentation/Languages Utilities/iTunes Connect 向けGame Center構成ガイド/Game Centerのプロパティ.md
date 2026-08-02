---
title: iTunes Connect 向けGame Center構成ガイド
apple_id: TP40014489
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide_Jpn/Chapters/GameCenterProperties.html
archived_at: '2026-07-27T06:57:09.116135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iTunes Connect 向けGame Center構成ガイド](%E6%A6%82%E8%A6%81.md)


[Next](%E6%9C%AC%E6%9B%B8%E3%81%AE%E6%94%B9%E5%AE%9A%E5%B1%A5%E6%AD%B4.md)[Previous](Game%20Center%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B.md)

# Game Centerのプロパティ

この付録では、ゲームの版とGame Centerの間のインタフェースの設定、またGame CenterでのLeaderboardおよびアチーブメントの表示のためにiTunes Connectが収集するメタデータについて説明します。

## Leaderboard

Leaderboardのメタデータにより、iTunes Connect内で各Leaderboardが識別され、スコアが記述され、Leaderboardの表示言語固有のテキストが収集されます。iTunes ConnectはLeaderboardの型とLeaderboardがアプリケーションとともに承認が済んでいる状態かどうかを示す状態のメタデータを追跡します。

アプリケーションの「Game Center」ページの「Leaderboard」セクションで次のプロパティを設定してください [(LeaderboardおよびLeaderboardセットを参照)](Leaderboard%E3%81%8A%E3%82%88%E3%81%B3Leaderboard%E3%82%BB%E3%83%83%E3%83%88.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltc)。

### Leaderboardのプロパティ

Leaderboardの主なプロパティでは、iTunes Connect内で各Leaderboardが識別され、スコアの構成と書式が記述されます。

| プロパティ | 解説 | 編集可能 |
| --- | --- | --- |
| Leaderboard Reference Name | Leaderboardの内部名。必須。iTunes Connect内でLeaderboardを検索する場合に使用する名前です。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |
| Leaderboard ID | Leaderboardの識別子として用いる文字列。このIDは100文字以下（1バイト文字の場合）に制限されています。これはGameKit APIにおける「カテゴリ」と同等です。一度設定したLeaderboard IDを後から編集することはできません。 | バイナリの登録後は編集できません。 |
| Score Format Type | スコアの書式型。整数、経過時間、金額など。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 |
| Score Submission Type | Leaderboardに表示されるスコア(「Best Score」または「Most Recent Score」)。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 |
| Sort Order | スコアの順序(「Low to High」または「High to Low」)。値が小さい方から順に表示する場合は「小→大」を指定します。大きい方から表示するならば「大→小」です。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 |
| Score Range | 64ビット符号付き整数で定義したスコアの範囲。値はlong型の最小値（-2^63）から最大値（2^63 - 1）までの範囲です。この範囲外のスコアは削除されます。スコア範囲の設定は任意ですが、追加する場合は両方の値を設定しなければならず、しかも等しい値であってはなりません。スコア範囲の設定を追加するか、または狭い範囲に変更してデータを制限すると、その範囲外のデータはすべて失われ、元に戻すことはできません。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |

### Leaderboardの表示言語に関するプロパティ

Leaderboardの言語に関するプロパティでは、Leaderboardの表示言語固有のテキストが収集されます。少なくとも1つの言語について、次のプロパティを入力する必要があります。

| プロパティ | 解説 | 編集可能 |
| --- | --- | --- |
| Language | Leaderboardの表示に用いる言語。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後   定義済みの言語を少なくとも1つ入力する必要があります。最後の言語は削除できません。 |
| Name | 指定した言語でのLeaderboardの参照名。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |
| Score Format | 指定した言語でスコアを表示するための書式。たとえば、アプリケーションのスコアがお金の場合、選択した言語に基づいて、異なる通貨単位を指定したい場合があります。このメニューの値はLeaderboardの「Score Format Type」を反映しています。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |
| Score Format Suffix（単数） | スコアの後に附加して表示する接尾辞（単数の場合）。接尾辞の指定は任意です。接尾辞は、Leaderboardに格納されるスコアの型を明確にするのに便利な機能です。「point」、「coin」、「hit」などといった接尾辞が考えられます。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |
| Score Format Suffix（複数） | スコアの後に附加して表示する接尾辞（複数の場合）。接尾辞の指定は任意です。接尾辞は、Leaderboardに格納されるスコアの型を明確にするのに便利な機能です。「points」、「coins」、「hits」などといった接尾辞が考えられます。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |
| Image | Leaderboardを表す、ローカライズ済みの画像。画像は `.jpeg`、 `.jpg`、 `.tif`、 `.tiff`、または `.png` ファイルで、512 x 512ピクセルまたは1024 x 1024ピクセル、72 dpi以上、およびRGB色空間でなければなりません。必要に応じて用意してください。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |

### Leaderboardの型

iTunes Connectは、Leaderboardの型のメタデータを追跡します。Leaderboardの型により、含まれるスコアが決まります。

| 型 | 解説 |
| --- | --- |
| 単体 | 他のLeaderboardと集約される単体Leaderboard。 |
| 集約 | いくつかの単体Leaderboardを集約して順位づけするもの。 |
| 被集約 | 他のLeaderboardとともに集約されている個々のLeaderboard。 |

### Leaderboardの状態

Leaderboardの状態は、そのLeaderboardがアプリケーションとともに承認が済んでいる状態かどうかを示します。

| 状態 | 解説 |
| --- | --- |
| In Review | Appleに登録し、審査を待っている状態。 |
| Live | アプリケーションとともに承認が済んでいる状態 |
| Not Live | 以前はLive状態であったが、対応するアプリケーションがグループに移行し、そのグループの承認が済んでいない状態。グループに追加されているLeaderboardのみに適用されます。 |

## アチーブメント

アチーブメントのメタデータにより、iTunes Connect内で各アチーブメントが識別され、スコアが記述され、アチーブメントの表示言語固有のテキストが収集されます。また、iTunes Connectはアチーブメントの型とLeaderboardがアプリケーションとともに承認が済んでいる状態かどうかを示す状態も追跡します。

アプリケーションの「Game Center」ページの「Achievements」セクションで次のプロパティを設定してください。 [(アチーブメントを参照)](%E3%82%A2%E3%83%81%E3%83%BC%E3%83%96%E3%83%A1%E3%83%B3%E3%83%88.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmznknltc)。

### アチーブメントのプロパティ

アチーブメントの主なプロパティでは、iTunes Connect内で各アチーブメントが識別され、アチーブメントの動作方法が記述されます。

| プロパティ | 解説 | 編集可能 |
| --- | --- | --- |
| Achievement Reference Name | アチーブメントの内部名。必須。iTunes Connect内でアチーブメントを検索する場合に使用する名前です。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |
| Achievement ID | アチーブメントの識別子として用いる文字列。このIDは100文字以下（1バイト文字の場合）に制限されています。一度設定したAchievement IDを後から編集することはできません。 | アチーブメントの保存後は編集できません。 |
| Point Value | アチーブメントの価値を表すポイント数。1つのアチーブメントにつき100ポイントが最高で、すべてのアチーブメントの合計が最大1,000ポイントです。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 |
| Hidden | 「Hidden」として設定されたアチーブメントは、プレーヤーが達成するまで、Game Centerには表示されません。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |
| Achievable More Than Once | このアチーブメントを繰り返し達成できるかどうかを表します。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |

### アチーブメントの表示言語に関するプロパティ

アチーブメントの言語に関するプロパティでは、アチーブメントの表示言語固有のテキストが収集されます。少なくとも1つの言語について、次のプロパティを入力する必要があります。

| プロパティ | 解説 | 編集可能 |
| --- | --- | --- |
| Language | アチーブメントの表示に用いる言語。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後   定義済みの言語を少なくとも1つ入力する必要があります。最後の言語は削除できません。 |
| タイトル | ローカライズ済みのタイトル。Game Centerにはこの文字列が表示されます。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |
| Pre-earned Description | アチーブメントの説明。Game Center上に、アチーブメント達成前に表示します。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |
| Earned Description | アチーブメントの説明。Game Center上に、アチーブメント達成後に表示します。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |
| Image | アチーブメントを表す、ローカライズ済みの画像。画像は `.jpeg`、 `.jpg`、 `.tif`、 `.tiff`、または `.png` ファイルで、512 x 512ピクセルまたは1024 x 1024ピクセル、72 dpi以上、およびRGB色空間でなければなりません。このプロパティは必須です。 | - バイナリが承認される前 - 「Developer Rejected」状態 - 「Rejected」状態 - 1つのバイナリが承認された後 |

### アチーブメントの状態

アチーブメントの状態は、そのアチーブメントがアプリケーションとともに承認が済んでいるかどうかを示します。

| 状態 | 解説 |
| --- | --- |
| In Review | Appleに登録し、審査を待っている状態。 |
| Live | アプリケーションとともに承認が済んでいる状態 |
| Not Live | 以前はLive状態であったが、対応するアプリケーションがグループに移行し、そのグループの承認が済んでいない状態。グループに追加されているアチーブメントのみに適用されます。 |

## グループのプロパティ

グループのプロパティにより、そのグループに含まれるアプリケーション、Leaderboard、アチーブメントが識別されます。アプリケーションの「Game Center」ページで次のプロパティを設定してください。 [(グループを参照)](%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqnbnknltc)。

| プロパティ | 解説 |
| --- | --- |
| Reference Name | 内部名。各グループに必須。iTunes Connectにはこの名前が表示されます。 |
| Apps in this Group | このグループに属するアプリケーション。 |
| Group Leaderboards | このグループで共有するLeaderboard。 |
| Group Achievements | このグループで共有するアチーブメント。 |
| Default Leaderboard | アプリケーションにデフォルトで表示されるLeaderboard。 |

## アプリケーションの版

アプリケーションの版のプロパティにより、iTunes Connectは特定のアプリケーションの版に適用されるGame Centerのプロパティを追跡できます。アプリケーションの「Version Details」ページでの選択 [(アプリケーションの版に対してGame Centerを有効にするを参照)](Game%20Center%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrwfvjvomrq)により、これらのメタデータのプロパティが設定されます。

| プロパティ | 解説 |
| --- | --- |
| Leaderboard | Leaderboardには、アプリケーションで上位を獲得したGame Centerユーザーのスコアが表示されます。いずれかの版のアプリケーションに対してGame Centerで使用されているLeaderboardを削除することはできません。アプリケーションごとに100個まで作成できます。必要に応じてゲームに取り入れてください。 |
| アチーブメント | 所定の目標を達成し、あるいはアクションを実行することによってプレーヤーが獲得できる一種の褒賞で、その内容はアプリケーションごとに異なります。いずれかの版のアプリケーションに対してGame Centerで使用されているアチーブメントを削除することはできません。必要に応じてゲームに取り入れてください。 |

[Next](%E6%9C%AC%E6%9B%B8%E3%81%AE%E6%94%B9%E5%AE%9A%E5%B1%A5%E6%AD%B4.md)[Previous](Game%20Center%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B.md)
