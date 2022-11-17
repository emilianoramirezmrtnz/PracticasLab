function contar
{
  param ([Parameter()] [int]$limite)
  $i = 0
  while ($i -lt $limite){
    Write-Host $i
    if ($i % 2 -eq 0){
      write-host $i " es par"
    }
  }
}


contar