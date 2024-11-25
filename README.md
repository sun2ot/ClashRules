<h1 align="center">
  <img src="./Clash_Logo.png" alt="Clash" width="200">
  <br>ClashRules<br>
</h1>

<h4 align="center">Personal use Clash rules, checking for omissions and filling gaps.</h4>

<p align="center">
  <a href="https://github.com/sun2ot/ClashRules/commits/main">
    <img src="https://img.shields.io/github/last-commit/sun2ot/ClashRules" alt="Github Commits">
  </a>
  <a href="https://github.com/tindy2013/subconverter">
    <img src="https://img.shields.io/badge/adapt-subconverter-green" alt="subconverter">
  </a>
  <a href="https://github.com/MetaCubeX/mihomo">
    <img src="https://img.shields.io/badge/for-mihomo-brightgreen">
  </a>
</p>

> 如 `config/emoji_new.toml|list` 显示异常，与目标国家样式不符等，请提交 issue

## 一、部分规则来源

1. [Semporia：Clash](https://github.com/Semporia/Clash)
2. [ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)
3. [blackmatrix7](https://github.com/blackmatrix7/ios_rule_script)
4. [Loyalsoldier](https://github.com/Loyalsoldier/clash-rules)
5. [AWAvenue-Ads-Rule](https://github.com/TG-Twilight/AWAvenue-Ads-Rule)
6. [ghip](https://github.com/sun2ot/GitHubIP2COS)

> china_ip_list 说明
>
> 1. `RuleSet/cnip*` 中的 ip 地址合并于 [china_ip_list](https://github.com/17mon/china_ip_list/blob/master/china_ip_list.txt)/[china-operator-ip](https://github.com/gaoyifan/china-operator-ip)
> 2. 为适应不同使用场景，统一 `IP-CIDR` 规则为 `clash-classic` 样式
> 3. 生成方法：将 `cnip.txt` 与批处理文件置于同一目录下，按需双击生成即可

## 二、使用方法

### 方法1. 手动修改配置文件

将最下方的 `rules` 和 `rule-providers` 复制粘贴/替换 到 Clash 的配置文件中

---

### 方法2. 自建 subconverter

1. 本地部署/线上部署 `subconverter`，见[github·subconverter](https://github.com/tindy2013/subconverter/blob/master/README-cn.md)
2. 复制仓库中的 `config/default.ini` 文件到 `subconverter` 根路径下的 `config/` 目录中
3. `all_base.tpl` 同理，建议阅读 `subconverter` 文档后**自行决定是否替换**
4. 修改 `subconverter` 根路径下的 `pref.toml` ，将 `api_access_token` 改为如下所示
   ```toml
   api_access_token = "随便设个密码"
   ```
5. 在 `subconverter` 根路径下的 `profiles/` 目录下(没有这个目录就建一个)，新建 `任意名称.ini` 文件，内容如下
   ```ini
   target=clash
   new_name=true
   url=订阅链接
   clash.dns=1   // 如果没有替换 `all_base.tpl`，就不要加这一行！！！
   config=config/default.ini
   exclude=(套餐|官网|频道)
   filename=任意名称
   expand=false
   ```
6. 通过 `subconverter` 订阅即可，订阅链接为
   `http(s)://你的ip(:25500)/getprofile?name=profiles/任意名称.ini&token=你设置的密码`

---

### 方法3. 利用现成的订阅转换网站，远程引用配置文件

1. 在订阅转换网站的页面中，会有一个下拉菜单让你选择**远程配置**，此处填写`https://raw.githubusercontent.com/sun2ot/ClashRules/main/public/default.ini`
   > Tips: 配置文件中已经嵌入了 emoji 配置
   >
2. 推荐在生成的订阅链接末尾加上参数 `&expand=false`
   > 这会让规则以 `rule-provider` 的形式进行订阅
   >
3. 其他更多参数见 `subconverter` [官方文档](https://github.com/tindy2013/subconverter/blob/master/README-cn.md#%E8%B0%83%E7%94%A8%E8%AF%B4%E6%98%8E-%E8%BF%9B%E9%98%B6)

---

## 三、附录

自用配置文件粘贴（↓）

```yaml
rules:
  - RULE-SET,SteamCN,🎮️ Steam
  - RULE-SET,Steam,🎮️ Steam
  - RULE-SET,Bahamut,📺️ 动画疯
  - RULE-SET,BilibiliHMT,🅱 Bilibili
  - RULE-SET,Microsoft,Ⓜ️ Microsoft
  - RULE-SET,Weibo,👊 微博
  - RULE-SET,GoogleVoice,📞 GoogleVoice
  - RULE-SET,OpenAI,🧠 OpenAI
  - RULE-SET,BardAI,🔭 BardAI
  - RULE-SET,direct,🎯 全球直连
  - RULE-SET,proxy,🚀 节点选择
  - RULE-SET,ghip,🚀 节点选择
  - RULE-SET,cnip,🎯 全球直连
  - RULE-SET,telegramcidr,🚀 节点选择
  - RULE-SET,AWAvenue-Ads-Rule-Clash,🚫 拦截
  - MATCH,🐟 漏网之鱼
rule-providers:
  SteamCN:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/SteamCN.yaml
    path: ./providers/rule-provider_SteamCN.yaml
    interval: 86400
  Steam:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Steam.yaml
    path: ./providers/rule-provider_Steam.yaml
    interval: 86400
  Bahamut:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Bahamut.yaml
    path: ./providers/rule-provider_Bahamut.yaml
    interval: 86400
  BilibiliHMT:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/sun2ot/ClashRules/main/RuleSet/BilibiliHMT.yaml
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
    url: https://raw.githubusercontent.com/sun2ot/ClashRules/main/RuleSet/Weibo.yaml
    path: ./providers/rule-provider_Weibo.yaml
    interval: 86400
  GoogleVoice:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleVoice/GoogleVoice.yaml
    path: ./providers/rule-provider_GoogleVoice.yaml
    interval: 86400
  OpenAI:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.yaml
    path: ./providers/rule-provider_OpenAI.yaml
    interval: 86400
  BardAI:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/BardAI/BardAI.yaml
    path: ./providers/rule-provider_BardAI.yaml
    interval: 86400
  direct:
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt
    path: ./providers/rule-provider_direct.yaml
    interval: 86400
  proxy:
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/proxy.txt
    path: ./providers/rule-provider_proxy.yaml
    interval: 86400
  ghip:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/sun2ot/GitHubIP2COS/master/tmp/ghip.yaml
    path: ./providers/rule-provider_ghip.yaml
    interval: 86400
  cnip:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/sun2ot/ClashRules/main/RuleSet/cnip/cnip.yaml
    path: ./providers/rule-provider_cnip.yaml
    interval: 86400
  telegramcidr:
    type: http
    behavior: ipcidr
    url: https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt
    path: ./providers/rule-provider_telegramcidr.yaml
    interval: 86400
  AWAvenue-Ads-Rule-Clash:
    type: http
    behavior: domain
    url: https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/Filters/AWAvenue-Ads-Rule-Clash.yaml
    path: ./providers/rule-provider_AWAvenue-Ads-Rule-Clash.yaml
    interval: 86400
```
