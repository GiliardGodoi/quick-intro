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

## Obtendo um processo e suas propriedades

### Obter todos os processos

```
>> Get-Process
```

Informações que são mostradas:

**Handles**: The number of process handles that the process opened. A handle is an integer that Windows assigns to processes. For instance, each process thread is typically assigned a handle.

**NPM(K)**: Non-paged memory the process is using, in kilobytes.

**PM(K)**: Pageable memory the process is using, in kilobytes.

**WS(K)**: Process working set, in kilobytes. The value refers to the number of memory pages that the process recently accessed.

**VM(M)**: Virtual memory the process is using.

**CPU(s)**: Processor time used on all processors, in seconds (!).

**Id**: Process ID.

**ProcessName**: Self-explanatory.

Retirado de [Timothy Warner 4sysops](https://4sysops.com/archives/powershell-get-process-managing-processes/)


### Obter um processo pelo ID ou pelo nome:

```
>> Get-Process python
```

ou

```
>> Get-Process 1356
```

Se o processo não existir (o nome ou pelo id) um erro é gerado.

### Listar as propriedades do processo

```
>> Get-Process 'python' | Format-List *
```

### Obter uma propriedade específica

```
>> Get-Process python -FileVersionInfo
```

### Obtendo informaçes detalhadas

```
>> Get-Process | Get-Member -MemberType Properties
```

```
>> Get-Process | Get-Member -Name CPU | Format-List *
```

* Informações muito úteis foram retiradas do [artigo](https://4sysops.com/archives/powershell-get-process-managing-processes/) de Timothy Warner para o site 4sysops.

* Explicações sobre as propriedades definidas para um processo encontradas na documentação oficial. [Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/api/system.diagnostics.process?redirectedfrom=MSDN&view=netcore-3.1#properties)

[link-0](https://blog.itpro.tv/get-process-powershell-command/)
