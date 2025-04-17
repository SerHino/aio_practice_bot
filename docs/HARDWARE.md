# Вимоги до апаратного забезпечення

## Мінімальна конфігурація
| Компонент       | Вимоги                          |
|-----------------|---------------------------------|
| CPU             | 2 ядра (x86_64)                 |
| RAM             | 2 GB                            |
| Disk            | 10 GB (SSD recommended)         |
| Network         | 1 Gbps, 5 MBit/s bandwidth      |

## Рекомендована конфігурація
| Компонент       | Вимоги                          |
|-----------------|---------------------------------|
| CPU             | 4 ядра (ARM64/x86_64)           |
| RAM             | 4 GB                            |
| Disk            | 50 GB NVMe                      |
| Backup          | Щоденні снапшоти БД             |

## Архітектура
```mermaid
graph LR
    A[Cloudflare CDN] --> B[Load Balancer]
    B --> C[Bot Instance 1]
    B --> D[Bot Instance 2]
    C & D --> E[PostgreSQL Cluster]
    E --> F[Backup Server]