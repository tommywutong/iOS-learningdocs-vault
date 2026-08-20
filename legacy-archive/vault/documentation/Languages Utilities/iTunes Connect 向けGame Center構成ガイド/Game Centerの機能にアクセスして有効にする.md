---
title: iTunes Connect 向けGame Center構成ガイド
apple_id: TP40014489
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide_Jpn/Chapters/AccessAndEnable.html
archived_at: '2026-07-27T06:57:09.005385Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iTunes Connect 向けGame Center構成ガイド](%E6%A6%82%E8%A6%81.md)


[Next](Leaderboard%E3%81%8A%E3%82%88%E3%81%B3Leaderboard%E3%82%BB%E3%83%83%E3%83%88.md)[Previous](%E6%A6%82%E8%A6%81.md)

# Game Centerの機能にアクセスして有効にする

iTunes ConnectではGame Center情報が2つのレベルで表示されます。アプリケーションレベルでは、Leaderboardおよびアチーブメントの詳細をすべて設定できます。版レベルでは、その版のアプリケーションに関連付けるLeaderboardおよびアチーブメントを指定します。このセクションでは、2つの設定レベルへのアクセス方法について説明します。

__注意：__ Game Centerの機能にアクセスできるのは、Admin、Legal、Technicalのいずれかの役割を持つiTunes Connectユーザのみです。ユーザの役割の割り当てについての詳細は、 iTunes Connectユーザのセットアップを参照してください。

## アプリケーションの「Game Center」ページを開く

アプリケーションでGame Centerの使用を開始するには、アプリケーションの「Game Center」ページを開きます。初めてこのページを開く場合、Game Centerに対してアプリケーションを有効にします。

![bullet](attachments/Resources/1282/Images/task_2x.png)iTunes Connect上でアプリケーションの「Game Center」ページに切り替えるには

1. Apple IDユーザ名とパスワードを使って、 [iTunes Connect](https://itunesconnect.apple.com) にサインインします。
2. 「Manage Your Apps」をクリックします。

   （原归档配图获取待重试：`gc_login_2x.png`）
3. 管理するアプリケーションを選択します。

   最近使用したアプリケーションのリストに表示されない場合、次の方法で探します。

   - 「See All」をクリックして、組織内のすべてのアプリケーションのリストを表示します。

     列の見出しをクリックしてリストを並べ替えたり、「Page」コントロールを使用してリスト内のページ間を移動したりできます。

     （原归档配图获取待重试：`apps_see_all_list_2x.png`）
   - 「Recent Activity」リストの下にある「Search」セクションの欄を使用します。

     （原归档配图获取待重试：`search_autocomplete_2x.png`）
4. 「Manage Game Center」をクリックします。

   （原归档配图获取待重试：`gc_manage_gc_2x.png`）
5. 以前にアプリケーションをGame Centerに対して有効にしたことがある場合、「Game Center」ページが表示されます。

   このアプリケーションをGame Centerに対して初めて設定する場合、Game Centerを有効にするよう求められます。次のいずれかを選択します。

   - Game Centerをこのアプリケーション専用に設定する場合、「Enable for Single Game」を選択します。
   - Game Centerコンポーネントを複数のアプリケーションで使用する場合、「Enable for Group Games」を選択します。

   適切な「Game Center」ページが表示されます。

このページから以下のGame Centerコンポーネントを設定できます。 [LeaderboardおよびLeaderboardセット](Leaderboard%E3%81%8A%E3%82%88%E3%81%B3Leaderboard%E3%82%BB%E3%83%83%E3%83%88.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrnknltc)、 [アチーブメント](%E3%82%A2%E3%83%81%E3%83%BC%E3%83%96%E3%83%A1%E3%83%B3%E3%83%88.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmznknltc)、 [グループ](%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqnbnknltc)。

## アプリケーションに対してGame Centerを有効にする

iTunes Connectには、アプリケーションに対してGame Centerを有効にする場所が2つあります。

- アプリケーション情報の「Game Center」ページです。「App Summary」ページから「Manage Game Center」をクリックして、アプリケーションの「Game Center」ページを開きます。

  詳しくは、 [iTunes Connect上でアプリケーションの「Game Center」ページに切り替えるにはを参照してください](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvooa)。

  「Game Center」ページでは、アプリケーションで使用するすべてのGame Centerコンポーネントを設定します。このページでGame Centerを有効にすることにより、アプリケーションとGame Centerとの間で通信を行ったり、 [Game CenterのメタデータをアプリケーションのiTunes Connectレコードに追加したり(Game Centerのプロパティを参照)](Game%20Center%E3%81%AE%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrzfvjvomi)することが可能になります。
- アプリケーションの版の「Versions Details」ページ「App Summary」ページで特定のアプリケーションの版の「Version Details」をクリックして、アプリケーションの「Version·Details」ページを開きます。

  詳しくは、 [アプリケーションの版に対してGame Centerを有効にするを参照してください](Game%20Center%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrwfvjvomrq)。

  「Version Details」ページには、このアプリケーションの版に対してGame Centerの設定を有効にする個々のオプションがあります。テストが完了し、アプリケーションを登録する準備ができた時点で、これらのオプションを設定します。詳しくは、 [アプリケーションの版に対してGame Centerを有効にするを参照してください](Game%20Center%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrwfvjvomrq)。

アプリケーションがGame Centerを通じて構成済みのコンポーネントにアクセスできるようにするには、Game Centerを両方の場所で有効にする必要があります。

## Game Centerを利用不可能に設定する

アプリケーションのある版が承認されるまで、版に対してGame Centerを利用不可能に設定できます。この操作によって、どの版に対してもGame Centerを利用できなくなります。Game Centerがアプリケーションの特定の版を利用できないよう無効化するには、 [Game Centerに対してアプリケーションのある版を無効にするにはを参照してください](Game%20Center%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmrwfvjvomzy)。

![bullet](attachments/Resources/1282/Images/task_2x.png)アプリケーションがGame Centerを利用できないよう無効化するには

1. アプリケーションの「Game Center」ページを開きます [(アプリケーションの「Game Center」ページを開くを参照)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobzfvbuqmryfvjvonrv)。
2. 「Game Center」セクションでトグルをクリックして、Game Centerを無効にします。

[Next](Leaderboard%E3%81%8A%E3%82%88%E3%81%B3Leaderboard%E3%82%BB%E3%83%83%E3%83%88.md)[Previous](%E6%A6%82%E8%A6%81.md)
