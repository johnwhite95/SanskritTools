# SanskritTools
## Overview
A toolkit for the Sanskrit language. Currently supports noun declension and
transliteration from Devanagari to Latin alphabet.

## Some examples



```python
import sanskrit_tools as st
```


```python
st.decline("phala", "neut")
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>case</th>
      <th>singular</th>
      <th>dual</th>
      <th>plural</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Nom.</td>
      <td>phalam</td>
      <td>phale</td>
      <td>phalāni</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Voc.</td>
      <td>phala</td>
      <td>phale</td>
      <td>phalāni</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acc.</td>
      <td>phalam</td>
      <td>phale</td>
      <td>phalāni</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ins.</td>
      <td>phalena</td>
      <td>phalābhyām</td>
      <td>phalaiḥ</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dat.</td>
      <td>phalāya</td>
      <td>phalābhyām</td>
      <td>phalebyaḥ</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Abl.</td>
      <td>phalāt</td>
      <td>phalābhyām</td>
      <td>phalebyaḥ</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Gen.</td>
      <td>phalasya</td>
      <td>phalayoḥ</td>
      <td>phalānām</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Loc.</td>
      <td>phale</td>
      <td>phalayoḥ</td>
      <td>phaleṣu</td>
    </tr>
  </tbody>
</table>
</div>




```python
st.romanize("कठोपनिषद")
```




    'कठोपनिषद → kaṭhopaniṣada'




```python
st.conjugate("nṛt", "4")
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Singular</th>
      <th>Dual</th>
      <th>Plural</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First</th>
      <td>nṛtyami</td>
      <td>nṛtyavaḥ</td>
      <td>nṛtyamaḥ</td>
    </tr>
    <tr>
      <th>Second</th>
      <td>nṛtyasi</td>
      <td>nṛtyathaḥ</td>
      <td>nṛtyatha</td>
    </tr>
    <tr>
      <th>Third</th>
      <td>nṛtyati</td>
      <td>nṛtyataḥ</td>
      <td>nṛtyanti</td>
    </tr>
  </tbody>
</table>
</div>


