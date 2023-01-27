rule-providers:
  CustomizeProxy:
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/CustomizeProxy.yaml
    path: ./ruleset/CustomizeProxy.yaml
    interval: 604800
  CustermizeDirect:
    type: http
    behavior: domain
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
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/cncidr.txt"
    path: ./ruleset/cncidr.yaml
    interval: 86400
  direct:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/direct.txt"
    path: ./ruleset/direct.yaml
    interval: 86400
rules:
  - RULE-SET,CustermizeProxy,🚀 节点选择
  - RULE-SET,CustermizeDirect,DIRECT
  - RULE-SET,CustermizeReject,🛑 拦截广告
  - RULE-SET,Weibo,👊 微博
  - RULE-SET,SteamCN,DIRECT
  - RULE-SET,Steam,🎮 Steam
  - RULE-SET,reject,🛑 拦截广告
  - RULE-SET,proxy,🚀 节点选择
  - RULE-SET,Bahamut,📺 动画疯
  - RULE-SET,BilibiliHMT,🅱️ 哔哩哔哩
  - RULE-SET,cncidr,DIRECT
  - RULE-SET,direct,DIRECT
  - GEOIP,LAN,DIRECT
  - MATCH,🚀 节点选择
