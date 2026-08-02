---
title: iTunes Connect 向けGame Center構成ガイド
apple_id: TP40014489
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide_Jpn/Chapters/DistributingGameCenterApps.html
archived_at: '2026-07-27T06:57:09.093563Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iTunes Connect 向けGame Center構成ガイド](%E6%A6%82%E8%A6%81.md)


[Next](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md)[Previous](%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E3%83%86%E3%82%B9%E3%83%88%E3%81%99%E3%82%8B.md)

# Game Centerアプリケーションを配布する

アプリケーションをApp StoreまたはMac App Storeに登録する準備ができたら、iTunes Connectの「Version Details」ページを使用します。ここで、アプリケーションのこの版にGame Centerの機能を組み込み、サポートするLeaderboardとアチーブメントを指定します。

## アプリケーションの版に対してGame Centerを有効にする

アプリケーションの「Version Details」ページで、アプリケーションのこの版に適用するGame Centerの機能を有効にします。

- Game Centerを有効にします。
- アプリケーションのこの版でサポートするLeaderboardを選択します。
- アプリケーションのこの版でサポートするアチーブメントを選択します。
- どのアプリケーションや版との互換性を持つかかも選択します。

Game Centerの機能の有効化は、 アプリケーションの登録で説明するアプリケーション登録プロセス全体の一部です。

![bullet](attachments/Resources/1282/Images/task_2x.png)アプリケーションのある版をGame Center対応として有効化するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](Game%20Center%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%81%A6%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 「Versions」セクションで、Game Centerに対して有効にする版の横の「View Details」をクリックします。
3. 「Game Center」セクションでスイッチをクリックしてGame Centerを有効にします。
4. アプリケーションがLeaderboardセットを使用し、この版と組にして登録するLeaderboardがある場合は、Leaderboardセット情報を次のように編集します。

   1. 「Leaderboard Sets」セクションで、「Edit」をクリックします。
   2. 「Add」ポップアップメニュー(+)を使用して、登録するLeaderboardを含むLeaderboardセットを選択します。
   3. 右側のペインで、そのセットから登録する個々のLeaderboardを選択します。

      （原归档配图获取待重试：`gc_app_version_lb_2x.png`）
   4. 「Save」をクリックします。
5. この版と組にして登録するLeaderboardがある場合は、Leaderboards情報を次のように編集します。

   アプリケーションがLeaderboardセットを使用し、そのセットからLeaderboardを選択した場合、このステップを省略できます。

   1. 「Leaderboards」セクションで「Edit」をクリックします。
   2. 登録するLeaderboardまたはLeaderboardセットを選択します。

      （原归档配图获取待重试：`gc_app_version_select_lb_2x.png`）
   3. 「Save」を押してください。
6. この版と組にして登録するアチーブメントがある場合は、「Achievements」セクションを次のように編集します。

   1. 「Achievements」セクションで「Edit」をクリックします。
   2. 登録するアチーブメントを選択します。
   3. 「Save」ボタンを押してください。
7. アプリケーションがグループに属する場合、またはこのアプリケーションにほかのアプリケーションとの互換性を持たせる場合、「Multiplayer Compatibility」セクションを次のように編集します。

   1. 「Multiplayer Compatibility」セクションで「Edit」をクリックします。
   2. (アプリケーションリストの下にある)「Add」ポップアップメニュー(+)から互換アプリケーションを選択します。

      （原归档配图获取待重试：`gc_mc_edit_2x.png`）

      「Add」ポップアップメニュー(+)には、追加可能なGame Center対応の各アプリケーションの名前とプラットフォームが表示されます。
   3. 登録するアプリケーションとの互換性を持たせるアプリケーションの版を選択します。
   4. 「Save」をクリックします。
8. 「Ready to Upload Binary」ボタンをクリックします。

## アプリケーションでGame Centerを無効にする

アプリケーションのある版が承認済みであれば、すべての版にわたってGame Centerを無効にすることはできません。必要に応じて、更新時に新しい版のGame Centerプロパティを個別に変更する必要があります。Game Centerに対してアプリケーションのある版を無効にするには、マルチプレーヤーの互換性設定を変更する必要があります [(アプリケーションのある版をGame Center対応として有効化するにはを参照)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrwfvjvomrz)。

__注意：__ アプリケーションの現在の版でGame Centerを無効にしても、Game Centerで使用中のLeaderboardは引き続き使用できます。

![bullet](attachments/Resources/1282/Images/task_2x.png)Game Centerに対してアプリケーションのある版を無効にするには

1. アプリケーション情報ページから、編集するアプリケーションの版の「Version Details」を開きます。
2. 「Game Center」セクションで「Enabled」ボタンをクリックし、Game Centerを無効にします。

[Next](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md)[Previous](%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E3%83%86%E3%82%B9%E3%83%88%E3%81%99%E3%82%8B.md)
