# Материалы для студентов

Дисциплина «Методы оптимизации в разработке программных решений». Скрипты и шаблоны для командного проекта. Скопируйте нужное в свой репозиторий: скрипты — в `scripts/`, шаблоны — в соответствующие каталоги.

Требования: Python 3.9+. Для графиков нужен `pip install matplotlib`, остальное работает без внешних библиотек.

## Скрипты (`scripts/`)

| Скрипт | Лабораторная | Назначение |
|---|---|---|
| `release_planner.py` | ЛР 1 | Выбор состава релиза: задача о рюкзаке 0-1 с зависимостями и обязательными историями. Сравнивает жадное решение (по v/w, как WSJF) с точным (метод ветвей и границ) |
| `pert_cpm.py` | ЛР 1 | Оценки PERT, ранние и поздние сроки, резервы, критический путь, вероятность уложиться в срок, граф в формате Mermaid |
| `monte_carlo.py` | ЛР 1, ЛР 4 | Вероятностный прогноз срока выполнения бэклога по истории пропускной способности |
| `flow_metrics.py` | ЛР 4 | Сбор данных из GitHub API и расчёт метрик DORA и потока; CFD, контрольная диаграмма, пропускная способность |

### Быстрый старт на примерах

```bash
cd scripts
python release_planner.py ../examples/backlog.csv --capacity 28
python pert_cpm.py ../examples/tasks.csv --deadline 14 --mermaid
python monte_carlo.py --history 3 5 2 4 6 3 4 5 --backlog 40
python flow_metrics.py report --data ../examples/data --out ../examples/report
python monte_carlo.py --csv ../examples/report/throughput_weekly.csv --backlog 8
```

При ёмкости 28 в примере видно, что жадный выбор по v/w не оптимален.

### Сбор метрик по своему репозиторию (ЛР 4)

```bash
export GITHUB_TOKEN=...   # fine-grained token с правом чтения репозитория
python flow_metrics.py collect --repo owner/project --deploy-workflow deploy.yml --out data
python flow_metrics.py report --data data --out ../docs/04-metrics
```

Чтобы метрики считались корректно, с первой недели проекта соблюдайте соглашения:

* начиная работу над задачей, назначьте исполнителя или поставьте метку `in progress`;
* закрывайте задачу, когда изменение слито и развёрнуто (по вашему Definition of Done);
* каждое изменение кода проходит через pull request с `Closes #N`;
* развёртывание — отдельный workflow (например, `deploy.yml`) в ветке `main`;
* инциденты и откаты оформляйте задачами с меткой `incident`; закрывайте их после восстановления.

Для GitLab и других платформ заполните CSV вручную или выгрузкой из трекера (формат описан в начале `flow_metrics.py` и показан в `examples/data/`).

## Шаблоны (`templates/`)

| Файл | Куда положить | Лабораторная |
|---|---|---|
| `.github/PULL_REQUEST_TEMPLATE.md` | `.github/` | ЛР 2 |
| `.github/CODEOWNERS` | `.github/` | ЛР 2 |
| `.github/workflows/ci-example.yml` | `.github/workflows/ci.yml` | ЛР 2 |
| `load/booking_k6.js` | `load/` | ЛР 3 |
| `docs/team-agreement.md` | `docs/01-planning/` | ЛР 1 |
| `docs/retro.md`, `docs/experiment.md` | `docs/04-metrics/` | ЛР 4 |

## Примеры (`examples/`)

* `backlog.csv` — бэклог сервиса бронирования переговорных (value, effort, зависимости, must);
* `tasks.csv` — задачи MVP с трёхточечными оценками и зависимостями;
* `data/` — синтетические данные процесса команды за семестр (задачи, pull request, развёртывания).
