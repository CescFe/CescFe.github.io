# Editorial Denes website

<div align="center">

[![Preview](assets/img/about_banner.jpg)](https://CescFe.github.io)

[![GitHub release](https://img.shields.io/github/v/release/CescFe/CescFe.github.io)](https://github.com/CescFe/CescFe.github.io/releases/latest)
[![GitHub license](https://img.shields.io/github/license/alshedivat/al-folio?color=blue)](https://github.com/alshedivat/al-folio/blob/master/LICENSE)

</div>

## Context

This is a modest project with the aim of providing Editorial Denes that allows them to achieve an online presence. The development is iterative: firstly a minimal functionality website has been launched, but the plan is to improve and expanded it gradually.

## Apply Prettier formatter

Apply prettier formatter to all files:

```
npx prettier . --write
```

Apply prettier formatter to a specific file:

```
npx prettier _news/guia_practica_verbs_valencians.md --write
```

Check if files are compliant with prettier:

```
npx prettier . --check
```

## Run the website locally

1. `docker compose pull`
2. `docker compose up`

## Sync with upstream

1. `git fetch --no-tags upstream`
2. `git merge upstream/main`

## License

The theme is available as open source under the terms of the [MIT License](https://github.com/alshedivat/al-folio/blob/main/LICENSE).

Originally, **al-folio** was based on the [\*folio theme](https://github.com/bogoli/-folio) (published by [Lia Bogoev](https://liabogoev.com) and under the MIT license). Since then, it got a full re-write of the styles and many additional cool features.

This repository is a fork of the [al-folio](https://github.com/alshedivat/al-folio.git).
