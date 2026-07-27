---
title: LeetCode Best Time to Buy and Sell Stock IV(k不重疊最大子段和)線性解法
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2015-03-27-leetcode-best-time-to-buy-and-sell-stock-iv'
original_language: en
published: 2015-03-27
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:13df7c47b02dda98'
translated: false
---

> 原文：[LeetCode Best Time to Buy and Sell Stock IV(k不重疊最大子段和)線性解法](https://maskray.me/blog/2015-03-27-leetcode-best-time-to-buy-and-sell-stock-iv)　·　MaskRay (宋方睿)

[2015-03-27](https://maskray.me/blog/2015-03-27-leetcode-best-time-to-buy-and-sell-stock-iv)

# LeetCode Best Time to Buy and Sell Stock IV(k不重疊最大子段和)線性解法

## 題目描述

[Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Credits: Special thanks to @Freezen for adding this problem and creating all test cases.

## 分析

在[https://leetcode.com/discuss/26745/c-solution-with-o-n-klgn-time-using-max-heap-and-stack](https://leetcode.com/discuss/26745/c-solution-with-o-n-klgn-time-using-max-heap-and-stack)看到，但沒說清理由。今天在地鐵上把前後都想清楚了，特此記錄。

令**價格向量爲**，**天數爲**。問題要求給出個**買入時刻**和個**賣出時刻**，滿足，使最大。

另外，這個問題等價於求出的差分向量的**k不重疊最大子段和**。下面給出一個線性算法，但沒有用到。

不失一般性，可以要求每個爲**局部極小值**，滿足或，且；每個爲**局部極大值**，滿足，且或。若最優方案不滿足這個條件，可以調整和以滿足這個條件，仍保持最優性。

先線性掃描，得到所有(上文定義的)局部極小和極大值。把它們按指標(向量中位置)順序排序，指標最小的若是局部極大值則捨棄，指標最大的若是局部極小值也捨棄。餘下的序列滿足局部極小和局部極大交替出現，且局部極小值先出現。設該序列爲，長度爲，把和配對，稱爲一個**pv對**(valley和peak)，性質是。

下面研究一下最佳方案的性質。

對於一個pv對，第天會買入或不作操作，不會賣出；第天會賣出或不作操作，不會買入。一個pv對並非捆綁的，即第天買入不意味着在第天賣出，可以在之後的某個pv對賣出。最佳買入時刻和賣出時刻(不超過對)一定在這個指標裏。

設的利益爲。我們設法變換這個pv對，得到若干不超過個新的pv對(可能會有，也不再保證)，使得按利益從大到小選取不超過個(因爲可能有負收益)，其利益和等於題目所求的最大收益。變換過程中的所有pv對稱爲**候選pv對**。

考慮相鄰兩個候選pv對：、，四個指標對應四個元素：。若4個數互不相等，則用0~3表示相對大小，有6種情形：

- 0123。由於，不應在第天賣出後在第天買入。若兩相鄰候選pv對滿足此情形，可保證1處不會賣出，2處不會買入，因此可以把這兩個pv對替換成一個pv對：，稱該操作爲**合併**。合併操作使pv對數目減少一，可以看作01的peak改變了，但其valley不變。
- 0213。可以把這兩個pv對變換成：，注意第二個pv對的p和v顺序顛倒了，稱這個操作爲**重組**。重組後pv對數目不變，收益和守恆，但重組後兩pv對的收益較大值增大了。若兩個pv對只能取一個，則應取收益較大的那個，因此重組是有利的。重組操作的valley也不變。枚舉四個點可能取的操作，可以發現重組不會使最佳方案變差。
- 2301。特徵是前一個pv對的valley小於後一個pv對的valley。考慮最佳方案可能在四個點取的操作：

    - 只有一個買入點。應放在0處。
    - 只有一個賣出點。應放在3處。
    - 一個賣出點後跟一個買入點。應放在3處和0處。
    - 一個買入點後跟一個賣出點。兩種可能：2處和3處，或0處和1處。
    - 其他。分析方法和上面類似。

  另外在這種情形下，23和之後的某個pv對合併或重組並非最優。合併或重組滿足valley不變，即使01與之後的pv對合併或重組了，這兩個pv對也不會再滿足合併或重組條件。
- 1203。和上一種情形特徵相同，結論相同。
- 1302。和上一種情形特徵相同，結論相同。
- 0312。合併或重組並非最優。但12可能會與之後的pv對合併或重組，回到0123或0213兩種情形，從而滿足合併或重組條件。

4個數若有相等，亦可歸入上述6種情形。

注意合併和重組都滿足valley不變，且有益的合併或重組會使peak增大，使得更容易滿足完成未來的合併或重組條件。這說明只要合併或重組有益，就應貪心進行。

另外“一旦不滿足合併或重組條件，則之後也不再滿足”。我們可以用棧維護候選pv對，表示可能會和未來的某個pv對重組或合併。從棧底到棧頂的各pv對滿足三個單調性：一是位置單調遞增，二是相鄰兩pv對滿足，三是。

棧初始爲空，另外維護一個隊列。按指標的遞增順序掃描各候選pv對，若棧頂與掃描到的pv對滿足2301、1203或1302(特徵是前一個pv對的valley小於後一個pv對的valley)，則應彈出棧頂，插入到隊列中。彈出若干pv對直到滿足不再出現這三種情形。

假如棧非空且棧頂與掃描到的pv對滿足0123或0213，則應根據之前的說明進行合併或重組，彈出的pv對都應插入到隊列裏。彈出若干pv對直到滿足不再出現這兩種情形。然後把掃描到的pv對壓棧。

所有pv對掃描完後，棧中相鄰元素滿足0312，全部彈出並插入到隊列裏。

隊列中所有元素即爲變換後的候選pv對。按利益從大到小排序，選取不超過個利益非負的，其利益和等於題目所求的最大收益。這一步可以用quick select(C++的`nth_element`)在線性時間內計算：選取利益第大的，則排在它前面的元素收益都不小於它。

## 實現

代碼見[https://github.com/MaskRay/LeetCode/blob/master/best-time-to-buy-and-sell-stock-iv.cc](https://github.com/MaskRay/LeetCode/blob/master/best-time-to-buy-and-sell-stock-iv.cc)。

另外此題也在[http://codeforces.com/problemset/problem/391/F3](http://codeforces.com/problemset/problem/391/F3)出現。網路上找到的實現都是基於差分向量的，較複雜。
