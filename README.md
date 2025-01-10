# Factorització de Polinomis

Aquest projecte proporciona eines per factoritzar polinomis i realitzar altres operacions matemàtiques com el Teorema del Residu, divisibilitat i la regla de Ruffini.

## Funcionalitats

1. **Factorització de polinomis**: Descompon polinomis en els seus factors.
2. **Teorema del residu**: Calcula el residu d'un polinomi dividit per un binomi (x - a).
3. **Divisibilitat**: Troba divisors enters d'un polinomi.
4. **Regla de Ruffini**: Aplica la regla de Ruffini per dividir un polinomi entre un binomi.

## Requisits

Aquest projecte requereix Python i les següents biblioteques:

- `math`
- `functools`
- `sympy`

Per instal·lar les dependències necessàries, pots executar:

```bash
pip install sympy
```
## Ús

### Exemples d'ús

#### Factoritzar un polinomi
1. Selecciona l'opció `F` al menú.
2. Introdueix el grau del polinomi i els seus coeficients.
3. El programa retornarà els factors i les solucions possibles.

#### Teorema del residu
1. Selecciona l'opció `T` al menú.
2. Introdueix el polinomi i el valor de "a".
3. El programa calcularà el residu.

#### Regla de Ruffini
1. Selecciona l'opció `R` al menú.
2. Introdueix el polinomi i el valor de "a".
3. El programa aplicarà la regla de Ruffini i mostrarà el resultat i el residu.

## Estructura del codi

- **Imports**: Inclou les biblioteques necessàries.
- **Funcions**: Funcions per factoritzar, calcular residus, trobar divisors i aplicar Ruffini.
- **Interacció amb l'usuari**: Un menú interactiu que guia l'usuari a través de les funcionalitats del programa.

## Errors i excepcions

El programa maneja els següents errors:

- **Entrada invàlida**: Mostra un missatge quan l'usuari introdueix dades incorrectes.
- **Operacions impossibles**: Per exemple, factoritzar polinomis amb delta negatiu o sense divisors enters.

## Contribució

Si vols contribuir al projecte:

1. Fes un fork del repositori.
2. Crea una branca amb la teva funcionalitat: `git checkout -b nova-funcionalitat`.
3. Fes un commit amb els teus canvis: `git commit -m "Afegeix nova funcionalitat"`.
4. Fes un push a la branca: `git push origin nova-funcionalitat`.
5. Obre una pull request.

## Llicència

Aquest projecte està sota la llicència MIT. Consulta el fitxer `LICENSE` per a més informació.

---

## Autoria

Aquest projecte ha estat creat per **Hackerjosep4**.
