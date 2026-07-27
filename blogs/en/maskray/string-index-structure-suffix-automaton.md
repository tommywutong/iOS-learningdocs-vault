---
title: 'String index structure: suffix automaton'
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2013-05-10-suffix-automaton'
original_language: en
published: 2013-05-10
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2848668d27e003a3'
translated: false
---

> 原文：[String index structure: suffix automaton](https://maskray.me/blog/2013-05-10-suffix-automaton)　·　MaskRay (宋方睿)

[2013-05-10](https://maskray.me/blog/2013-05-10-suffix-automaton)

# String index structure: suffix automaton

## Suffix automaton

Deterministic acyclic finite state automaton，也叫directed acyclic word graph(DAWG)，是一個識別若幹字串的無環DFA。識別若干字串的所有DAWG中，存在唯一一個狀態數最少的DAWG，稱作minimal DAWG，即識別這個字串集的DFA。

DAWG在有些文獻中也指識別一個字串的所有後綴的自動機，這種用法有個更常見的名稱：suffix automaton，此時該自動機可以看做是字串所有後綴的DAWG。

## 定義

- Factor，即子串。
- ，的所有子串。比如。
- 表示的所有後綴的集合。比如。
- 表示中所有出現位置右邊的串的集合。比如對於，其。
- 表示中和的出現位置集合相同，即。
- 爲串中子串的suffix function：的最長後綴，滿足。 無定義。當定義在的所有後綴上時就得到了suffix link，因此suffix function是suffix link的推廣，用於處理factor的集合。
- 用上標表示函數應用的次數，即，，……

## 一些引理

在考慮時，對於的兩個子串和，定義和在一個集合中當且僅當，把看作一個狀態。 添加一個新字符後，易知會產生一個新狀態，因爲它與已有的集合都不相同。 下面的三條引理說明了添加字符後，集合是如何演變爲的，從而知道大多數狀態不會發生變化，狀態不會合併，且最多隻有一個狀態會分裂成兩個。

### 引理1

給添加字符後的變化：

對於的一個子串，若的最後一個字符不是，則添加字符後所屬狀態沒有發生變化。

### 引理2

令爲在中出現過的的最長後綴，那麼對於的任意兩個子串：

證明：

- 若，則是中出現過的的一個後綴，由定義知。
- 存在最大的非負整數使得， 由性質有， 又，故。 因此即。
- 因此。對稱地，。 所以和同時在中或同時不在。
- 根據引理1，即與的關係知。

這條引理說明，對於的一個後綴，若，則添加字符後所屬狀態沒有發生變化。

### 引理3

依舊令表示在中出現過的的最長後綴。

下面的引理則說明，中與等價的集合，在末尾添加新字符後是怎樣變化的：

- 。

    - 由引理1和知
    - 由知，故。因此
    - 前兩式得
- ，其中為滿足的中最長子串，且不是的後綴。

    - 和都不是的後綴

如果第二個分類不爲空，則中與等價的集合會分裂成兩個集合：的等價類和的等價類，從而多出一個狀態。

## 性質

長度爲1的串的suffix automaton，其狀態數爲2。新增字符後，會多出一個新狀態。根據引理3，所屬狀態可能會分裂成兩個狀態。因此添加一個字符會使狀態數增加1或2。對於，suffix automaton的狀態數。而狀態數的下界爲，當串爲全`a`時即可取到下界。

另外對於，邊數的下界爲，上界爲。

記爲節點的suffix function，它表示的等價類，其中是表示的等價類中的任意一個串。

## 構建

採用一個在線算法構建字串的suffix automaton，從從空串對應的suffix automaton(僅含一個頂點)出發，逐個添加中的字符。維護變量表示最後添加的頂點，它表示當前已添加的字串的所屬狀態。 每個狀態記錄，表示表示的串的suffix function對應的狀態。另外記錄，表示的等價類中最長串的長度。

添加字符時有下面兩種情況：

- 未在中出現 只多了一個狀態，該狀態的suffix function爲起始狀態。 所有後綴的狀態都應添加在字符上的轉移，指向新狀態。方法是從出發，追溯得到的所有狀態都添加指向新狀態的邊。
- 在中出現 從出發，追溯，直到遇到第一個頂點存在字符上的轉移，設轉移到。 表示的最長串(長度爲)後添加就是(長度爲)。 的等價類則表示中與等價的所有。 然後再分兩種情況：

    - 若，則的長度大於等於中與等價的任一。的等價類(表示爲狀態)不會分裂。Suffix automaton只多了一個表示等價類的狀態，，其，包含與，因此設置。
    - 若，則存在，需要拆分爲兩個狀態，分別表示(狀態)和(新狀態)，繼承的所有邊，，需要修改爲。另外還要沿着，把沿路狀態在上的轉移改爲。

稍作修改該算法即可用於多串suffix automaton的構建。處理新字串時，把重置爲起始狀態，每次添加字符時，轉移至的狀態可能已在automaton中，無需創建。添加完字符後，可能有兩種取值，需要注意。

```c++
struct Node
{
  Node *f, *c[26];
  int len;
} pool[2*N], *tail, *pit;

void extend(int c)
{
  bool created = false;
  Node *p = tail, *x;
  if (p->c[c])
    x = p->c[c];
  else {
    created = true;
    x = pit++;
    x->len = p->len+1;
    for (; p && ! p->c[c]; p = p->f)
      p->c[c] = x;
  }
  if (! p)
    x->f = pool;
  else if (p->len+1 == p->c[c]->len) {
    if (created)
      x->f = p->c[c];
  } else {
    Node *q = p->c[c], *r = pit++;
    *r = *q;
    r->len = p->len+1;
    for (; p && p->c[c] == q; p = p->f)
      p->c[c] = r;
    q->f = r;
    if (created)
      x->f = r;
    else
      x = r;
  }
  tail = x;
}

{
  // string 0
  tail = pool;
  extend(0); extend(1); extend(2);

  // string 1
  tail = pool;
  extend(0); extend(2); extend(2);

  // string 2
  tail = pool;
  extend(2); extend(1); extend(1);
}
```

## 性質

- 另表示從開始，沿著函數回溯得到的所有狀態，accepting states是。
- Suffix automaton中所有邊形成一棵spanning tree。
- ，所以對於suffix automaton中任意頂點，
- 對於邊，，所以可以對所有頂點的值做計數排序，達到拓撲排序的效果。

## 輔助數據結構

設有定義(在自動機中)，

表示對應的集合中的最長串長度，即第一次出現的位置的右邊串長度。計算方式如下：

是第一次出現的位置。

表示對應的集合中的最短串長度，即最後一次出現的位置的右邊串長度。計算方式如下：

是最後一次出現的位置。

是在串裏的出現次數。

對所有狀態拓撲排序後，根據其逆序計算即可求出各個狀態的、和值。

## 應用

- 列出模式串在文本串中所有匹配位置(all occurrences)。
- 求出最長的出現至少次的子串。尋找最深的節點滿足，其深度即爲答案。
- Ending factors。給定兩個串和，對於的所有前綴，求出的最長後綴爲的子串。可用於計算兩串的最長公共子串。
- Searching for rotations。給定兩個串和，的任意rotation(或稱爲conjugate)在中出現的位置。技巧是把和自身拼接，得到，它包含的個rotation，轉化爲和的ending factors問題。
- 個串的最長公共子串。求次ending factors。

## 相關數據結構

### Factor automaton

Suffix automaton有個類似的數據結構，稱作factor automaton，它識別一個字串的所有子串，可以看作識別所有子串的minimal DAWG。

求出的suffix automaton後，把所有狀態標記為accept state後就得到了識別所有子串的DAWG，但可能不是最簡的，做minimize即可得到factor automaton，而acyclic DFA可以用Revuz's algorithm在時間內求最簡表示。

反過來，可以通過factor automaton獲得suffix automaton。參見Maxime Crochemore、Christophe Hancart的《Automata for Matching Patterns》中的FA-to-SA。

### Suffix oracle和factor oracle

Suffix oracle是一種簡化的suffix automaton。

某次添加字符時，令表示在中出現過的的最長後綴，如果存在，那麼suffix automaton中會進行狀態分裂，而factor oracle不分裂，相當於把兩個狀態合併了。

Suffix oracle可以看作是suffix automaton合併了一些狀態後得到的自動機。其接受的串的集合是suffix automaton接受的串的集合的超集，也就是說它不會遺漏suffix automaton接受的串，但可能會有誤判。

Suffox oracle的優點是節點數為，比最壞情況下的suffix automaton大致少一半。邊數爲到。

把suffix oracle的所有狀態標記爲可接受即得到factor oracle，且已是最簡形態，無法minimize。

## 其他類似數據結構

### Position heap

比suffix tree簡單，存在一個離線構造算法，但實現複雜度不比suffix automaton低。

## 參考文獻

Allauzen C., Crochemore M., Raffinot M., Factor oracle: a new structure for pattern matching; Proceedings of SOFSEM’99; Theory and Practice of Informatics.

@article{Revuz:1992:MAD:135853.135907, author = {Revuz, Dominique}, title = {Minimisation of Acyclic Deterministic Automata in Linear Time}, journal = {Theor. Comput. Sci.}, issue_date = {Jan. 6, 1992}, volume = {92}, number = {1}, month = jan, year = {1992}, issn = {0304-3975}, pages = {181--189}, numpages = {9}, url = {http://dx.doi.org/10.1016/0304-3975(92)90142-3}, doi = {10.1016/0304-3975(92)90142-3}, acmid = {135907}, publisher = {Elsevier Science Publishers Ltd.}, address = {Essex, UK}, }
