# Quantum Espresso Study
Here, I am studying various materials using Quantum Espresso.
## How to run
1. Run SCF calculation
```bash
pw.x < inputs/{material}.scf.in > outputs/{material}.scf.out
```
2. Band calculation <br>
To get a band structure, more detailed (more k-points) energy calculation is needed (nscf).
```bash
pw.x < inputs/{material}.nscf.in > outputs/{material}.nscf.out
bands.x < inputs/{material}/bands.in > outputs/{material}.bands.out
```
After the run, you will get two outputs: .dat and .dat.gnu. 

3. DOS (Density of states) calculation <br>
Just like band calculation, DOS calculation also needs more detailed energy calculation at more k-points. So it takes longer runtime than scf.
```bash
dos.x < inputs/{material}.dos.in > outputs/{material}.dos.out
```