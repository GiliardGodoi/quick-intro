# PowerShell Commands

## Diretórios

### Navegar entre os diretórios
```
cd ./folder
cd ..
```

### Listar diretório
```
ls [./folder]
dir
```

### Copiando arquivos

```
Copy-Item [file-path-source] -Destination [file-path-dst]
copy [file-path-source] [file-path-dst]
```

### Movendo arquivos OU renomear arquivos

```
mv filename newfilename
mv filename folder/filename
```

### Remover arquivos

```
Remove-Item
rm [file-path]
rm [file-path] -r
```

## Programar desligamento

```
shutdown -s -t 600
shutdown -r -t 600
shutdown -s -c "Vai Dormir!"
shutdown -a
```

Opções:

    -s shutdown
    -r restart
    -a abort
    -t time in seconds
    -c message
