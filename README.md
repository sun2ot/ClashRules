```yaml
rule-providers:
  CustomizeProxy:
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/CustomizeProxy.yaml
    path: ./ruleset/CustomizeProxy.yaml
    interval: 604800
  CustermizeDirect:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/CustermizeDirect.yaml
    path: ./ruleset/CustermizeDirect.yaml
  CustermizeReject:
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/CustermizeReject.yaml
    path: ./ruleset/CustermizeReject.yaml
    interval: 604800
  Weibo:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/Weibo.yaml
    path: ./ruleset/Weibo.yaml
    interval: 604800
  reject:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/reject.txt
    path: ./ruleset/reject.yaml
    interval: 86400
  proxy:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt
    path: ./ruleset/proxy.yaml
    interval: 86400
  Bahamut:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Bahamut.yaml
    path: ./ruleset/Bahamut.yaml
    interval: 604800
  BilibiliHMT:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/BilibiliHMT.yaml
    path: ./ruleset/BilibiliHMT.yaml
    interval: 604800
  SteamCN:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/SteamCN.yaml
    path: ./ruleset/SteamCN.yaml
    interval: 604800
  Steam:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Steam.yaml
    path: ./ruleset/Steam.yaml
    interval: 604800
  cncidr:
    type: http
    behavior: ipcidr
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/cncidr.txt
    path: ./ruleset/cncidr.yaml
    interval: 86400
  direct:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/direct.txt
    path: ./ruleset/direct.yaml
    interval: 86400
rules: # 规则匹配顺序为从上之下，因此顺序极有讲究
  # 第一优先级为可直连可代理的 "两面派"
  - RULE-SET,Steam,🎮 Steam
  - RULE-SET,SteamCN,DIRECT
  - RULE-SET,Bahamut,📺 动画疯
  - RULE-SET,BilibiliHMT,🅱️ 哔哩哔哩
  - RULE-SET,Weibo,👊 微博
  # 第二优先级为(除开订阅规则的)客制化规则
  - RULE-SET,CustermizeDirect,DIRECT
  - RULE-SET,CustermizeProxy,🚀 节点选择
  - RULE-SET,CustermizeReject,🛑 拦截广告
  # 第三优先级为第三方订阅(代理>直连>拦截)
  - RULE-SET,proxy,🚀 节点选择
  - RULE-SET,cncidr,DIRECT
  - RULE-SET,direct,DIRECT
  - RULE-SET,reject,🛑 拦截广告 # 拦截放最后真不亏，指望dns层面拦截本来就是聊胜于无，更何况乱拦截还容易出问题
  - GEOIP,LAN,DIRECT
  # 兜底
  - MATCH,🚀 节点选择
```
