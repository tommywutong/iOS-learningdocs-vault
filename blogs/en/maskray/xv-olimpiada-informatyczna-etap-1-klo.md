---
title: XV Olimpiada Informatyczna - Etap 1 - klo
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2010-03-13-xv-olimpiada-informatyczna-etap-1-klo'
original_language: en
published: 2010-03-13
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:032c61786af1aacd'
translated: false
---

> 原文：[XV Olimpiada Informatyczna - Etap 1 - klo](https://maskray.me/blog/2010-03-13-xv-olimpiada-informatyczna-etap-1-klo)　·　MaskRay (宋方睿)

[2010-03-13](https://maskray.me/blog/2010-03-13-xv-olimpiada-informatyczna-etap-1-klo)

```article-inner
#include <cstdio>
#include <climits>
#include <algorithm>
using namespace std;

const int N = 100000;
int a[N];

struct Node *null, *pit, *root;
struct Node
{
    int key, size;
    long long sum;
    Node *ch[2];
    Node() {}
    Node(int key) : key(key), size(1), sum(key) {ch[0] = ch[1] = null; }
    void update() {
        size = ch[0]->size + 1 + ch[1]->size;
        sum = ch[0]->sum + key + ch[1]->sum;
    }
}pool[N+1];

void zag(Node *&x, int d)
{
    Node *y = x->ch[!d];
    x->ch[!d] = y->ch[d];
    y->ch[d] = x;
    y->size = x->size;
    y->sum = x->sum;
    x->update();
    x = y;
}

void maintain(Node *&x, int d)
{
    if (x == null) return;
    if (x->ch[d]->ch[d]->size > x->ch[!d]->size)
        zag(x, !d);
    else if (x->ch[d]->ch[!d]->size > x->ch[!d]->size)
        zag(x->ch[d], d), zag(x, !d);
    else return;
    maintain(x->ch[0], 0);
    maintain(x->ch[1], 1);
    maintain(x, 0);
    maintain(x, 1);
}

void insert(Node *&x, int key)
{
    if (x == null) {
        x = new Node(key);
        return;
    }
    int d = x->key < key;
    ++x->size;
    x->sum += key;
    insert(x->ch[d], key);
    maintain(x, d);
}

Node *erase(Node *&x, int key)
{
    if (x->key == key || key < x->key && x->ch[0] == null || key > x->key && x->ch[1] == null) {
        if (x->ch[0] == null || x->ch[1] == null) {
            Node *y = x;
            x = x->ch[x->ch[0] == null];
            return y;
        }
        Node *y = erase(x->ch[1], key-1);
        x->key = y->key;
        x->update();
        return null;
    }
    Node *y = erase(x->ch[x->key < key], key);
    x->update();
    return y;
}

long long tot, mid;
void count(Node *&x, int cnt)
{
    if (x->ch[0]->size == cnt) {
        mid = x->key;
        tot += x->ch[0]->sum + x->key;
    } else if (x->ch[0]->size > cnt)
        count(x->ch[0], cnt);
    else
        tot += x->ch[0]->sum + x->key,
        count(x->ch[1], cnt-x->ch[0]->size-1);
}

int main()
{
    pit = pool;
    root = null = new Node(0); null->size = 0; null->ch[0] = null->ch[1] = null;

    int n, k;
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);

    long long best = LLONG_MAX;
    int res1, res2, res3;
    for (int i = 0; i < k-1; i++)
        insert(root, a[i]);
    for (int i = k-1; i < n; i++) {
        insert(root, a[i]);
        tot = 0;
        count(root, k/2);
        long long t = mid*(k/2+1)-tot + root->sum-tot-mid*(k-k/2-1);
        if (t < best) {
            best = t;
            res1 = i-k+1;
            res2 = i;
            res3 = mid;
        }
        erase(root, a[i-k+1]);
    }

    printf("%lld\n", best);
    for (int i = res1; i <= res2; i++)
        a[i] = res3;
    for (int i = 0; i < n; i++)
        printf("%d\n", a[i]);
}
```
