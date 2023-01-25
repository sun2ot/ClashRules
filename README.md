I'll add it later

```yaml
rule-providers:
  CustermizeDirect: # 自定义直连
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/CustermizeDirect.yaml
    path: ./ruleset/CustermizeDirect.yaml
    interval: 604800
  Weibo: # 微博
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/Weibo.yaml
    path: ./ruleset/Weibo.yaml
    interval: 604800

  # https://github.com/Loyalsoldier/clash-rules
  reject: # 广告拦截
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/reject.txt
    path: ./ruleset/reject.yaml
    interval: 86400
  proxy: # 代理
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt"
    path: ./ruleset/proxy.yaml
    interval: 86400

  # https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash/Providers/Ruleset
  Bahamut: # 巴哈姆特
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Bahamut.yaml
    path: ./ruleset/Bahamut.yaml
    interval: 604800
  BilibiliHMT: # 哔哩哔哩 港澳台番剧
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/BilibiliHMT.yaml
    path: ./ruleset/BilibiliHMT.yaml
    interval: 604800
  SteamCN: # steam国内直连
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/SteamCN.yaml
    path: ./ruleset/SteamCN.yaml
    interval: 604800
  Steam: # steam
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Steam.yaml
    path: ./ruleset/Steam.yaml
    interval: 604800
  ChinaDomain: # 国内域名
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/ChinaDomain.yaml
    path: ./ruleset/ChinaDomain.yaml
    interval: 604800
rules:
  - DOMAIN-SUFFIX,googleapis.cn,🚀 节点选择
  - RULE-SET,CustermizeDirect,DIRECT
  - RULE-SET,Weibo,👊 微博
  - RULE-SET,SteamCN,DIRECT
  - RULE-SET,Steam,🚀 节点选择
  - RULE-SET,reject,🛑 拦截广告
  - RULE-SET,proxy,🚀 节点选择
  - RULE-SET,Bahamut,📺 动画疯
  - RULE-SET,BilibiliHMT,🅱️ 哔哩哔哩
  - RULE-SET,ChinaDomain,DIRECT
  - GEOIP,LAN,DIRECT
  - MATCH,🚀 节点选择
  ```
