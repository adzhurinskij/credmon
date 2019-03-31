# Utility for checking credentials.

#### Installation

```bash
pip install credmon
```

#### Usage

```bash
credmon check config.yml
```

#### Config example

FTP:
```yml
- name: example.com
  type: ftp
  config:
    hostname: ftp.example.com
    username: secret
    password: secret
```

Modx:
```yml
- name: example.com
  type: modx
  config:
    url: https://example.com/manager/
    username: secret
    password: secret
```