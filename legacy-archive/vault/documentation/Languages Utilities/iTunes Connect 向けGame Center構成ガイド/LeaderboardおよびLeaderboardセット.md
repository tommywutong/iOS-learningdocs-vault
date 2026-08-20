---
title: iTunes Connect 向けGame Center構成ガイド
apple_id: TP40014489
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide_Jpn/Chapters/Leaderboards.html
archived_at: '2026-07-27T06:57:09.041263Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iTunes Connect 向けGame Center構成ガイド](%E6%A6%82%E8%A6%81.md)


[Next](%E3%82%A2%E3%83%81%E3%83%BC%E3%83%96%E3%83%A1%E3%83%B3%E3%83%88.md)[Previous](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md)

# LeaderboardおよびLeaderboardセット

ゲームに追加するLeaderboardごとに、iTunes Connectを使用して、順位づけするスコアとその表示方法を指定します。

（原归档配图获取待重试：`leaderboard_2x.png`）

ゲームでのLeaderboardの開発に関する詳細については、 『Game Centerプログラミングガイド』 の _“Leaderboard”を参照してください_。

iTunes Connectでは、次の設定を行います。

- 単体
- 集約Leaderboard
- Leaderboardセット
- Leaderboardの言語サポート

## 単体Leaderboardを作成する

単体Leaderboardを利用すると、プレーヤー同士が同じゲームでスコアを競うことができます。iTunes ConnectでLeaderboardを設定する場合、収集するスコアとスコアの並べ方などの詳細を指定します。Leaderboardを表示する言語ごとに、Leaderboardの名前、スコア書式、スコア単位を指定します。また、Leaderboardでスコアを示すためのローカライズされた画像も指定できます。

iTunes ConnectでアプリケーションのLeaderboardを設定できるのは、アプリケーションの状態が「In Review」以外である場合です。アプリケーションの承認済みの版にLeaderboardが表示された後は、Leaderboardを削除できません。

Leaderboardについての情報を入力する場合は、 [Leaderboardのプロパティ](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrzfvjvomjv) を参照してください。

![bullet](attachments/Resources/1282/Images/task_2x.png)単体Leaderboardを設定するには、

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 必要に応じて、Game Centerを有効にします。
3. 「Leaderboards」セクションで「Add Leaderboard」をクリックします。

   （原归档配图获取待重试：`gc_add_lb_2x.png`）
4. 表示されるダイアログで、単体Leaderboardのオプションを選択します。

   表示されるフォームには、 [Leaderboardのプロパティで説明されているLeaderboardのオプションがあります](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrzfvjvomjv)。
5. 「Leaderboard Reference Name」欄にLeaderboardの内部名を入力します。

   （原归档配图获取待重试：`gc_create_lb_2x.png`）

   後で言語サポートを追加する際、これとは別に、画面に表示されるローカライズ済みのLeaderboardの名前を入力することになります。
6. 「Leaderboard ID」欄にLeaderboard ID(英数字文字列)を入力します。

   Leaderboard IDは、Game Kitでは _カテゴリ_ とも呼ばれます。Leaderboardの保存後、この値は変更できません。
7. スコアの書式型を「Score Format Type」メニューから選択してください。
8. 保存するスコアの型を決定するために、「Best Score」または「Most Recent Score」を選択します。
9. スコアの整列順序として、「Low to High」または「High to Low」を選択します。

   たとえば、レースの最高タイムを表示するスコアでは、整列順序を「Low to High」にします。
10. 必要に応じて、スコアの範囲を「Score Range」欄に入力します。

    この範囲はスコアの取りうる(有効な)値を示します。プレーヤーのスコアがこの範囲外の場合、そのスコアは無視されます。
11. 「Add Language」をクリックして、スコアを表示するためのテキストを指定します。

    （原归档配图获取待重试：`gc_lb_add_lang_2x.png`）
12. 表示されるダイアログで表示テキストを設定します [(Leaderboardの表示言語を設定するを参照)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltemy)。

    アプリケーションがサポートする言語または地域ごとに、この手順を繰り返します。
13. 「Save」をクリックします。

    Leaderboardのリストに新しいLeaderboardが表示されます。

    （原归档配图获取待重试：`gc_add_lb_complete_2x.png`）

__重要：__ 「Ready for Sale」状態のアプリケーションにLeaderboardを追加すると、次の版を登録して審査を求める際、Leaderboardも自動的に登録されます。登録したくない場合は、「Version Details」ページのデフォルト設定を変更してください [(Game Centerアプリケーションを配布するを参照)](Game%20Center%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrwfvjvomq)。

## Leaderboardを設定する

複数のLeaderboardがある場合、次のことが可能です。

- デフォルトのLeaderboardの変更
- Leaderboardのプロパティの編集
- Leaderboardの表示順序の変更
- Leaderboardの削除

グループに追加されたLeaderboardの管理に関する詳細については、 [グループを設定するを参照してください](%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqnbnknltini)。

デフォルトのLeaderboardとは、Game CenterでユーザがLeaderboardを開いたとき、最初に表示されるLeaderboardのことです。最初に作成した単体Leaderboardが、自動的にデフォルトのLeaderboardとして設定されています。

![bullet](attachments/Resources/1282/Images/task_2x.png)デフォルトのLeaderboardを設定するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. デフォルトにするLeaderboardの行にある「Default」オプションを選択します。

アプリケーションの状態によって、編集可能なプロパティが制限されることがあります。アプリケーションを登録して審査を求める前であれば、Leaderboard ID以外のプロパティは変更できます。登録後は、ほとんどのプロパティは編集できません。編集できるプロパティの種類に関する詳細については、 [Leaderboardのプロパティ](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrzfvjvomjv) を参照してください。

![bullet](attachments/Resources/1282/Images/task_2x.png)Leaderboardの設定を編集するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 「Leaderboards」セクションで、編集するLeaderboardをクリックします(行の任意の場所をクリックします)。
3. 必要に応じてLeaderboardのプロパティを変更します。

   Leaderboardのプロパティは、 [Leaderboardのプロパティで説明されています](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrzfvjvomjv)。

   （原归档配图获取待重试：`gc_edit_lb_2x.png`）
4. 「Leaderboard Localization」セクションで、Leaderboardの表示テキストを変更する言語を選択します。

   詳しくは、 [Leaderboardの表示言語を設定するを参照してください](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltemy)。
5. 「Save」をクリックします。

Game Centerでは、iTunes Connectで表示されている順にLeaderboardがプレーヤーに表示されます。この順序はアプリケーションの「Game Center」ページで変更できます。

![bullet](attachments/Resources/1282/Images/task_2x.png)Leaderboardの順序を変更するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 「Leaderboard」セクションで順序を変更するLeaderboardを選択します。
3. 最初の列のアイコンを使用して、Leaderboardを表の新しい場所にドラッグします。

   （原归档配图获取待重试：`gc_lb_reorder_2x.png`）

Leaderboardの状態は、表の一番右の列に表示されます。取りうる状態については、 [Leaderboardの状態で説明されています](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrzfvjvomjy)。この列に「Delete」ボタンが現れていればこれ以外の状態であり、削除しても問題ありません。Game CenterでLeaderboardが使用できる状態になった後は、削除できません。

![bullet](attachments/Resources/1282/Images/task_2x.png)Leaderboardを削除するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 「Leaderboard」セクションで削除するLeaderboardを選択します。
3. 「Status」列で「Delete」をクリックします。

   Game CenterでそのLeaderboardがまだ使用されていない場合のみ、「Delete」ボタンが表示され有効になっています。
4. 「削除」をクリックして確認します。

## Leaderboardの表示言語を設定する

iTunes Connectでは、スコアそのものとは別に、Leaderboardのテキストを設定できます。そのため、アプリケーションがサポートする言語や地域ごとに、テキスト設定を繰り返すことができます。少なくとも1つの言語設定を入力する必要があります。Leaderboardの表示言語に関するプロパティの詳細については、 [Leaderboardの表示言語に関するプロパティ](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrzfvjvomjw) を参照してください。

![bullet](attachments/Resources/1282/Images/task_2x.png)Leaderboardの表示テキストを追加するには

1. Leaderboardをまだ作成していない場合は、Leaderboardを作成します [(単体Leaderboardを設定するにはを参照)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltcna)。
2. 「Add Leaderboard」ページの「Leaderboard Localization」セクションで、「Add Language」ボタンをクリックします。

   （原归档配图获取待重试：`gc_lb_add_lang_2x.png`）
3. 表示されるダイアログで、「Language」メニューから言語を選択します。
4. 「Name」欄にLeaderboardのローカライズされた参照名を入力します。

   たとえば、「Language」メニューから「Finnish」を選択した場合、「Name」欄にはフィンランド語によるLeaderboardの名前を入力してください。
5. ローカライズしたスコア書式を「Score Format」メニューから選択します。
6. 必要に応じて、「Score Format Suffix」欄にローカライズされたスコアの接尾辞を入力します。

   スコアと接尾辞の間に空白を挿入したい場合は、空白の後に続けて接尾辞を入力します。

   （原归档配图获取待重试：`gc_add_lang_form_2x.png`）

   「Score Format Suffix Plural」が表示されない場合、選択した言語では不要ということです。
7. 必要に応じて「Choose File」をクリック、Leaderboardを表すローカライズ済みの画像を選択します。
8. 「Save」をクリックします。
9. この手順を繰り返して別の言語を追加するか、「Save」をクリックしてこのLeaderboardの変更を適用します。

アプリケーションの状態が「In Review」以外であれば、Leaderboardの表示言語のプロパティを編集できます。編集できるプロパティの種類とタイミングについては、 [Leaderboardの表示言語に関するプロパティ](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrzfvjvomjw) を参照してください。

![bullet](attachments/Resources/1282/Images/task_2x.png)Leaderboardの表示言語を編集するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 「Leaderboards」セクションで、編集するLeaderboardを選択します。
3. 開いたページの「Leaderboard Localization」セクションで、編集する言語をクリックします。
4. 表示されるダイアログで、この言語のLeaderboardのテキストのプロパティを変更します。

   詳しくは、 [Leaderboardの表示言語に関するプロパティを参照してください](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrzfvjvomjw)。
5. 「Save」をクリックします。
6. 「Edit Leaderboard」ページで「Save」をクリックします。

言語を削除できるのは、「Edit Leaderboard」ページの「Leaderboard Localization」セクションに言語が複数ある場合に限ります。

![bullet](attachments/Resources/1282/Images/task_2x.png)Leaderboardの表示言語を削除するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 「Leaderboards」セクションで、編集するLeaderboardを選択します。
3. 削除する言語の行にある「Delete」ボタンを押します。
4. 「削除」をクリックして確認します。

## 集約Leaderboardを設定する

集約Leaderboardでは、複数の単体Leaderboardに載っているプレーヤーが順位づけられます。たとえば、レースゲームのレベルごとのラップタイムを扱うLeaderboardがある場合、そのゲームの全レベルにわたってプレーヤーのスコアを順位づける集約Leaderboardを設定できます。集約Leaderboardを作成するには、単体Leaderboardが2つ以上必要です。同じ集約Leaderboardに入れるLeaderboardは、スコアの書式や整列順序が同じでなければなりません。集約Leaderboardに関する情報を入力する場合は、 [Leaderboardのプロパティ](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrzfvjvomjv) を参照してください。

（原归档配图获取待重试：`gc_lb_concept_2x.png`）

作成した集約Leaderboardは、アプリケーションに設定されているほかのLeaderboardとともに管理できます。Leaderboardのリストでは、型はLeaderboardが集約されたことを意味します。集約Leaderboardに使用されたLeaderboardは、被集約Leaderboardとして表示されます。

__注意：__ App Storeでアプリケーションが使用できる状態になった後に集約Leaderboardを作成する場合、新しい集約Leaderboardでは新しいスコアのみが表示されます。子Leaderboardで以前に収集された値は集約Leaderboardには移行されません。

集約LeaderboardはLeaderboardセットとは異なります。集約Leaderboardは、複数のLeaderboardのスコアを1つにまとめたリストを提供します。LeaderboardセットはLeaderboardのコンテンツには影響せず、Leaderboardを整理するだけのものです。詳しくは、 [Leaderboardセットを設定するを参照してください](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltmny)。

![bullet](attachments/Resources/1282/Images/task_2x.png)Leaderboardを集約するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 集約する単体Leaderboardをまだ作成していない場合は作成します。

   集約するLeaderboardのスコア書式と整列順序が同じであることを確認します。詳しくは、 [単体Leaderboardを作成するを参照してください](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltiny)。
3. 「Leaderboards」セクションで「Add Leaderboard」をクリックします。
4. 表示されるダイアログで、集約Leaderboardのオプションを選択します。

   「Choose Combined Leaderboard」ボタンが無効になっている場合、この操作を実行する前に、単体Leaderboardを2つ以上作成する必要があります。
5. 「Leaderboard Reference Name」欄に集約Leaderboardの参照名を入力します。

   後で言語サポートを追加する際、集約Leaderboardの表示名を入力することになります。
6. 「Leaderboard ID」欄に集約Leaderboard ID(英数字文字列)を入力します。
7. 「Leaderboards to Combine」セクションで、集約するLeaderboardを2つ以上選択します。

   リストに表示されているLeaderboardのうち、スコア書式や整列順序の設定が同じものしか集約できません。リストが更新され、集約可能なLeaderboardのみが表示されます。

   （原归档配图获取待重试：`gc_lb_combine_2x.png`）
8. 「Add Language」をクリックして、集約Leaderboardのスコアを表示するためのテキストを指定します。

   （原归档配图获取待重试：`gc_lb_add_lang_2x.png`）
9. 表示されるダイアログで表示テキストを設定します [(Leaderboardの表示言語を設定するを参照)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltemy)。

   アプリケーションがサポートする言語または地域ごとに、この手順を繰り返します。
10. 「Save」をクリックします。

    Leaderboardのリストに新しい集約Leaderboardが表示されます。

## Leaderboardセットを設定する

Leaderboardセットでは、複数のLeaderboardを1つにまとめて整理します。たとえば、多数のレベルがあるゲームでLeaderboardセットを定義し、レベルごとのLeaderboardを整理できます。Leaderboardセットにより、アプリケーションごとに使用できるLeaderboardの数が増えます。Leaderboardセットを使用しない場合、アプリケーションが使用できるLeaderboardの最大数は100個です。Leaderboardセットを使用すると、アプリケーションで使用できるLeaderboardの最大数が500個になります(Leaderboardセットが100個ある場合)。Leaderboardセットには最大100個のLeaderboardを含めることができます。

Leaderboardセットを作成するには、アプリケーションに少なくとも1つのLeaderboardが作成されている必要があります。アプリケーションにLeaderboardセットを追加すると、その後に設定するLeaderboardはすべてLeaderboardセットに含める必要があります。

iOSの場合、iOS 7からLeaderboardセットを作成できます。OS X v10.9ではLeaderboardセットはサポートされていません。

ゲームでのLeaderboardセットの使用については、 Leaderboardセットを参照してください。

Leaderboardセットは集約Leaderboardとは異なります。Leaderboardセットは個々のLeaderboardのコンテンツに影響せず、Leaderboardを整理するものです。集約Leaderboardでは、複数のLeaderboardのスコアをまとめた1つのリストが提供されます。詳しくは、 [集約Leaderboardを設定するを参照してください](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltcny)。

### Leaderboardセットを作成する

Leaderboardセットを作成してアプリケーションのLeaderboardを整理するには、次の手順に従います。

- 最初のLeaderboardセットを作成します。
- 追加のLeaderboardセットを作成します。
- Leaderboardセットに新しいLeaderboardを直接追加します。

最初のLeaderboardセットを作成すると、iTunes Connectで、アプリケーションのすべての既存Leaderboardが少なくとも1つのLeaderboardセットに含まれている事が確認されます。Leaderboardと同様に、Leaderboardセットでも、アプリケーションがサポートする言語ごとに内部名、ID、表示テキストを設定する必要があります。

![bullet](attachments/Resources/1282/Images/task_2x.png)最初のLeaderboardセットを作成するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 「Leaderboards」セクションで、「Move All Leaderboards into Leaderboard Sets」をクリックします。

   （原归档配图获取待重试：`gc_lb_sets_initial_move_2x.png`）
3. 「Leaderboard Set Reference Name」欄に、Leaderboardセットの内部名を入力します。

   言語サポートを追加する際、これとは別に、画面に表示されるローカライズ済みのLeaderboardの名前を入力することになります。
4. 「Leaderboard Set ID」欄に、Leaderboardセットの一意のIDを入力します。
5. 「Continue」をクリックします。
6. 「Move Leaderboards Into Sets」ページで、「Add to Leaderboard Set」をクリックします。

   （原归档配图获取待重试：`gc_lb_set_add_to_set_2x.png`）
7. 「Add Leaderboard to Set」ダイアログで、このLeaderboardセットに含める各Leaderboardを設定します。

   - Leaderboardを選択します。
   - 言語を選択します。
   - Leaderboardのこの言語での表示名を設定します。
   - 「Save」をクリックします。（原归档配图获取待重试：`gc_lb_add_to_set_dialog_2x.png`）

   このとき、このLeaderboardセットのコンテキストで、Leaderboardに別の名前を付けることができます。たとえば、「Level 1 Laps」という単体Leaderboardがレベル1のLeaderboardセットに含まれているとき、「Laps」という名前を付けることができます。

   このセットに含めるLeaderboardごとにこの手順を繰り返します。
8. すべてのLeaderboardがセットに含まれていることを確認します。

   次のいずれかの方法を取ることができます。

   - Leaderboardを既存のセットに追加します。そのためには、ステップ6～7に従って、「Leaderboard Set」メニューでLeaderboardセットを選択し、「Add to Leaderboard Set」をクリックします。
   - 「Add Leaderboard Set」をクリックして、別のLeaderboardセットを作成します [(新しいLeaderboardセットを追加するにはを参照)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltmoi)。
9. 「Move Leaderboards Into Sets」ページで「Add Language」をクリックし、Leaderboardセットの表示名を指定します。
10. 表示されるダイアログで、Leaderboardセットの言語、表示名、画像を選択します。
11. 「Save」をクリックします。
12. アプリケーションがサポートする言語または地域ごとに、ステップ9～11を繰り返します。
13. 「Save」をクリックして新規Leaderboardセットの設定を適用します。

アプリケーションに新しいLeaderboardセットを追加して、Leaderboardの表示をさらにカスタマイズできます。各セットでは、特定のLeaderboardがセット内で表示される方法を指定することができます。同じLeaderboardを複数の異なるセットに含めたり、各セット内でLeaderboardに別の表示名を設定したりすることができます。

![bullet](attachments/Resources/1282/Images/task_2x.png)新しいLeaderboardセットを追加するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 「Leaderboards」セクションで、「Add Leaderboard Set」をクリックします。

   （原归档配图获取待重试：`gc_lb_set_add_set_redbox_2x.png`）
3. 表示されたダイアログの「Leaderboard Set Reference Name」欄に、Leaderboardセットの内部名を入力します。

   言語サポートを追加する際、これとは別に、画面に表示されるローカライズ済みのLeaderboardの名前を入力することになります。
4. 「Leaderboard Set ID」欄に、Leaderboardセットの一意のIDを入力します。
5. 「Add to Leaderboard Set」をクリックして、Leaderboardをセットに追加します。

   （原归档配图获取待重试：`gc_lb_set_add_new_redbox_2x.png`）
6. 「Add Leaderboard to Set」ダイアログで、このLeaderboardセットに含める各Leaderboardを設定します。

   - Leaderboardを選択します。
   - 言語を選択します。
   - Leaderboardのこの言語での表示名を設定します。
   - 「Save」をクリックします。（原归档配图获取待重试：`gc_lb_add_to_set_dialog_2x.png`）

   このとき、このLeaderboardセットのコンテキストで、Leaderboardに別の名前を付けることができます。たとえば、「Level 1 Laps」という単体Leaderboardがレベル1のLeaderboardセットに含まれているとき、「Laps」という名前を付けることができます。

   このセットに含めるLeaderboardごとに、このステップを繰り返します。
7. セット内でのLeaderboardの順序を確認します。

   表内でのLeaderboardの表示順序は、Game Centerでの表示順序です。
8. 「Add Leaderboard Set」ページで「Add Language」をクリックし、Leaderboardセットの名前を表示する言語を1つ以上設定します。
9. 表示されるダイアログで、言語、表示名、Leaderboardセットの画像を選択します。

   「Language」フィールドと「Display Name」フィールドは必須です。「Image」フィールドの設定は任意です。
10. 「Save」を押してください。
11. ステップ8～10を繰り返し、追加の言語のサポートを追加します。
12. 「Save」をクリックして新しいLeaderboardセットの設定を保存します。

アプリケーションでLeaderboardセットの使用を開始した後は、新しいLeaderboardの作成方法は少し異なってきます。設定を保存する前に、新しいLeaderboardをLeaderboardセットと関連付ける必要があります。

![bullet](attachments/Resources/1282/Images/task_2x.png)新しいLeaderboardを作成し、Leaderboardセットに追加するには

1. “単体Leaderboardを設定するには” [で説明されているステップに従って新しいLeaderboardを作成します](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltcna)。
2. 「Add Leaderboard」ページで「Add to a Leaderboard Set」をクリックします。

   このページにこのセクションが表示されるのは、アプリケーションのLeaderboardセットを設定した後のみです。

   （原归档配图获取待重试：`gc_lb_add_lb_to_set_2x.png`）
3. 「Add Leaderboard to Leaderboard Set」ダイアログで、Leaderboardセットを選択します。
4. このLeaderboardがLeaderboardセットに表示されるときの表示言語と表示名を設定します。

   アプリケーションがサポートする言語または地域ごとに、このステップを繰り返します。
5. 「Save」をクリックします。
6. 「Leaderboard Localization」セクションで「Add Language」をクリックし、単体Leaderboardの設定を完了します。

   詳しくは、 [Leaderboardの表示テキストを追加するにはを参照してください](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltemq)。
7. 「Save」をクリックします。

Leaderboardセットの順序は、セットの名前を希望する位置にドラッグすることで並べ替えることができます。Leaderboardセットの名前をクリックしてコンテンツを編集するか、その中に含まれているLeaderboardの順序を変更します。

（原归档配图获取待重试：`gc_lb_sets_reorder_2x.png`）

どのLeaderboardがどのLeaderboardセットに含まれているかを確認するには、「View Leaderboards in Leaderboard Sets」をクリックします。アプリケーションに対して定義されているすべてのLeaderboardが名前と参照IDごとに表示され、各Leaderboardがどのセットに表示されるかがチェックで示されます。

（原归档配图获取待重试：`gc_lb_sets_matrix_2x.png`）

### Leaderboardセットを削除する

Leaderboardセットを削除するには、セットに含まれるすべてのLeaderboardが別のセットにも含まれていることを確認したうえで、削除するセットからLeaderboardを削除する必要があります。Leaderboardが別のセット内にある状態にならないかぎり、LeaderboardセットからLeaderboardをすることは削除できません。

![bullet](attachments/Resources/1282/Images/task_2x.png)Leaderboardセットを削除するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 削除するLeaderboardを選択します。
3. Leaderboardセットをクリックして設定ページを開きます。

   （原归档配图获取待重试：`gc_lb_sets_cursor_2x.png`）
4. 「Leaderboards in This Set」セクションで、Leaderboardごとに「Remove」をクリックします。

   （原归档配图获取待重试：`gc_lb_sets_remove_lb_2x.png`）
5. 関連するすべてのLeaderboardの削除後、「Done」をクリックします。
6. 「Game Center」ページで「Delete」をクリックし、Leaderboardセットを削除します。

   （原归档配图获取待重试：`gc_lb_sets_delete_2x.png`）
7. 「削除」をクリックして確認します。

アプリケーションに含まれるLeaderboardが100個以下である場合は、「Remove All Leaderboards in Leaderboard Sets」をクリックすると、現在のLeaderboardセットがすべて削除されます。Leaderboardが100個を超えるアプリケーションでは、このオプションは表示されません。「Remove All Leaderboards in Leaderboard Sets」ボタンを使用するためには、100個を超えているLeaderboardを削除する必要があります。

### LeaderboardセットをグループのLeaderboardセットに併合する

ゲームをグループに併合すると、複数のゲーム感でLeaderboardセットを共有できます。各ゲームに対する最大 500個のLeaderboardと 100個のLeaderboardセットという制限に変更はありません。しかし、グループ内にあるLeaderboardとLeaderboardセットの合計数は、この制限を超えることができます。各グループの 500個のLeaderboardと100個のLeaderboardセットという最大値に、グループ内にあるゲームの数を乗算したものが上限になります。たとえば、3つのゲームがあるグループでは、合計で1500個までのLeaderboardと300個までのLeaderboardセットをグループ内に保持することができます。グループの作成および管理の詳細については、 [グループを参照してください](%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqnbnknltc)。

グループへのゲームの併合は1つずつ行います。Leaderboardセットが設定された単体ゲームをゲームに併合できるのは、次の2つの条件のどちらかが当てはまる場合です。

- グループがすでにLeaderboardセットを使用している。
- このゲームから新規グループを作成している。

Leaderboardセットが設定されていないゲームを、Leaderboardセットが設定されたグループに併合することはできません。既存のグループに単体ゲームを併合するには、単体ゲームにLeaderboardセットを追加しておく必要があります。

同様に、Leaderboardセットの設定されたゲームを、Leaderboardセットが設定されていない既存のグループに併合することもできません。このゲームをグループに併合するには、グループ内のすべてのLeaderboardをLeaderboardセットに移動しておく必要があります。

![bullet](attachments/Resources/1282/Images/task_2x.png)グループが使用するすべてのLeaderboardをLeaderboardセットに変換するには

1. グループ内の1つのアプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。

   アプリケーションはグループに含まれているため、表示されるページにはそのグループのGame Centerオプションがあります。
2. 「Group Leaderboards」セクションで、「Move All Leaderboards into Leaderboard Sets」をクリックします。
3. 表示されるダイアログに、最初の新しいLeaderboardセットの情報を入力します。

   - 「Leaderboard Set Reference Name」欄に、Leaderboardセットの内部名を入力します。
   - 「Leaderboard Set ID」欄に、Leaderboardセットの一意のIDを入力します。

     ゲームがグループの一部になると、各LeaderboardとLeaderboardセットのセットIDの前に自動的に接頭辞 `grp.` が付きます。LeaderboardとLeaderboardセットのセットIDを変更することができますが、 `grp.` という接頭辞は新しい名前でもそのまま使用する必要があります。
4. 「Continue」をクリックして、「Move Leaderboards into Sets」ページを開きます。

   このページから次のことができます。

   - 「Add Leaderboard Set」をクリックして、ステップ3で説明した、グループの追加のLeaderboardセットを作成します。
   - 「Add to Leaderboard Set」をクリックして、ページ上部で選択されているセットにLeaderboardを追加します。

     Leaderboardを選択し、セットに含まれているこのLeaderboardの表示名を指定するよう求められます。アプリケーションがサポートする言語や地域ごとに表示名を指定します。
   - 「Add Language」をクリックし、ページ上部で選択されているLeaderboardセットの表示名を指定します。

     このLeaderboardセットの表示名を指定するよう求められます。アプリケーションがサポートする言語や地域ごとに表示名を指定します。また、Leaderboardセットの画像も言語ごとに指定できます。
5. グループのすべてのLeaderboardを1つ以上のLeaderboardセットに割り当てたら、「Save」をクリックします。

## iTunes ConnectにLeaderboardのメタデータを一括アップロードする

iTunes Connectで多数のLeaderboardを設定する場合、Transporterを使用して、Leaderboardおよびその他のiTunes Connect構成メタデータをApp Storeパッケージとして一括配信できます。詳しくは、 _『App Metadata Specification(アプリケーションメタデータ規格)』_ および _『Transporter Quick Start Guide(Transporterクイックスタートガイド)』を参照してください_。iTunes Connectユーザは、「Manage Your Apps」ページ下部の「Deliver Your Apps」でこれらのドキュメントを参照できます。

（原归档配图未能恢复：`links_bottom_manage_apps_2x.png`）

[Next](%E3%82%A2%E3%83%81%E3%83%BC%E3%83%96%E3%83%A1%E3%83%B3%E3%83%88.md)[Previous](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md)
