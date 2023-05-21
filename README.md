# qCaster

Schedule future casts on Farcaster

<!-- Badge row 1 - status -->

[![GitHub contributors](https://img.shields.io/github/contributors/wbnns/qcaster)](https://github.com/wbnns/qcaster/graphs/contributors)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/w/wbnns/qcaster)](https://github.com/wbnns/qcaster/graphs/contributors)
[![GitHub Stars](https://img.shields.io/github/stars/wbnns/qcaster.svg)](https://github.com/wbnns/qcaster/stargazers)
![GitHub repo size](https://img.shields.io/github/repo-size/wbnns/qcaster)
[![GitHub](https://img.shields.io/github/license/wbnns/qcaster?color=blue)](https://github.com/wbnns/qcaster/blob/main/LICENSE)

<!-- Badge row 2 - links and profiles -->

[![Website wbnns.com](https://img.shields.io/website-up-down-green-red/https/wbnns.com.svg)](https://wbnns.com/)
[![Log](https://img.shields.io/badge/blog-up-green)](https://log.wbnns.com/)
[![Twitter wbnns](https://img.shields.io/twitter/follow/wbnns?style=social)](https://twitter.com/wbnns)

<!-- Badge row 3 - detailed status -->

[![GitHub pull requests by-label](https://img.shields.io/github/issues-pr-raw/wbnns/qcaster)](https://github.com/wbnns/qcaster/pulls)
[![GitHub Issues](https://img.shields.io/github/issues-raw/wbnns/qcaster.svg)](https://github.com/wbnns/qcaster/issues)

## Description

qCaster is a command-line based Ruby gem that integrates with Warpcast. It reads a file that contains a Cast on each line and processes the Casts every 72 minutes. In addition, it Casts 'Gm' at 9:30 AM and 'Gn' at midnight.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'qcaster'
