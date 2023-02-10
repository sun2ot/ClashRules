## 上游规则来源

https://github.com/Semporia/Clash
https://github.com/Loyalsoldier/clash-rules
https://github.com/ACL4SSR/ACL4SSR

```yaml
rules:
  - RULE-SET,SteamCN,🎯 全球直连
  - RULE-SET,Steam,🚀 节点选择
  - RULE-SET,Bahamut,📺️ 动画疯
  - RULE-SET,BilibiliHMT,🅱 Bilibili
  - RULE-SET,Microsoft,Ⓜ️ Microsoft
  - RULE-SET,Weibo,🚀 节点选择
  - RULE-SET,CustomizeDirect,🎯 全球直连
  - RULE-SET,CustomizeProxy,🚀 节点选择
  - RULE-SET,CustomizeReject,🛑 拦截
  - RULE-SET,telegramcidr,🚀 节点选择
  - RULE-SET,proxy,🚀 节点选择
  - RULE-SET,cncidr,🎯 全球直连
  - RULE-SET,direct,🎯 全球直连
  - RULE-SET,reject,🛑 拦截
  - MATCH,🐟 漏网之鱼
rule-providers:
  SteamCN:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/SteamCN.yaml
    path: ./providers/rule-provider_SteamCN.yaml
    interval: 86400
  Steam:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Steam.yaml
    path: ./providers/rule-provider_Steam.yaml
    interval: 86400
  Bahamut:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Bahamut.yaml
    path: ./providers/rule-provider_Bahamut.yaml
    interval: 86400
  BilibiliHMT:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/RuleSet/BilibiliHMT.yaml
    path: ./providers/rule-provider_BilibiliHMT.yaml
    interval: 86400
  Microsoft:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/Semporia/Clash/master/Rule/Microsoft.yaml
    path: ./providers/rule-provider_Microsoft.yaml
    interval: 86400
  Weibo:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/RuleSet/Weibo.yaml
    path: ./providers/rule-provider_Weibo.yaml
    interval: 86400
  CustomizeDirect:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/RuleSet/CustomizeDirect.yaml
    path: ./providers/rule-provider_CustomizeDirect.yaml
    interval: 86400
  CustomizeProxy:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/RuleSet/CustomizeProxy.yaml
    path: ./providers/rule-provider_CustomizeProxy.yaml
    interval: 86400
  CustomizeReject:
    type: http
    behavior: classical
    url: https://ghproxy.com/https://raw.githubusercontent.com/zhihang-yi/ClashRules/main/RuleSet/CustomizeReject.yaml
    path: ./providers/rule-provider_CustomizeReject.yaml
    interval: 86400
  telegramcidr:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/telegramcidr.txt
    path: ./providers/rule-provider_telegramcidr.yaml
    interval: 86400
  proxy:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt
    path: ./providers/rule-provider_proxy.yaml
    interval: 86400
  cncidr:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/cncidr.txt
    path: ./providers/rule-provider_cncidr.yaml
    interval: 86400
  direct:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/direct.txt
    path: ./providers/rule-provider_direct.yaml
    interval: 86400
  reject:
    type: http
    behavior: domain
    url: https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/reject.txt
    path: ./providers/rule-provider_reject.yaml
    interval: 86400
```
