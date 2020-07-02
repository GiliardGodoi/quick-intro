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
    
## Start-Process

```
Start-Process -FilePath "python" -ArgumentList "main.py" -Verb RunAs
```

See documantation about [Start-Process](https://docs.microsoft.com/pt-br/powershell/module/microsoft.powershell.management/start-process?view=powershell-6)

## Definir uma prioridade difente para o processo

```
>> Get-Process -ProcessName 'python'

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    224      43    54548      15164       4,81   5548   9 python
    129      15    12236       7436   4.877,86   5976   9 python
    198      34    44448      12848       3,13   8012   9 python
    198      34    44436      12800       3,41  13132   9 python
```

Poderá aparecer uma lista como a demostrada acima. Para obter um único processo, podemos passar o Id. 


```
>> Get-Process -Id 8012

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    198      34    44448      12848       3,13   8012   9 python
```

Se retornado um único objeto, podemos fazer algo como:

```
>> (Get-Process -Id 8012).prioryticlass = "High"
```

Podemos saver mais nesse [link aqui](https://gallery.technet.microsoft.com/scriptcenter/Set-the-process-priority-9826a55f).
