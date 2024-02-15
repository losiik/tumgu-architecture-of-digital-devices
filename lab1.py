import numpy as np
import matplotlib.pyplot as plt

def generate_signal(frequency, time_end, ts):
    T = 1 / frequency  # Период
    signal = [4.5 if (i // (T / 2)) % 2 == 0 else 0.5 for i in np.arange(0, time_end, ts)]
    return np.array(signal)

def simulate_cascade(signal, T, A, Umin, Umax, ts):
    U = np.zeros(len(signal))
    U_distorted = np.zeros(len(signal))
    logic_state = np.zeros(len(signal))
    logic_state_distorted = np.zeros(len(signal))
    for n in range(1, len(signal)):
        U_distorted[n] = U_distorted[n-1] + ts * (signal[n] - U_distorted[n-1]) / T + np.random.uniform(-A, A)
        U[n] = U[n-1] + ts * (signal[n] - U[n-1]) / T
        if logic_state[n-1] == 0 and U[n] < Umax:
            logic_state[n] = 0
        elif logic_state[n-1] == 1 and U[n] > Umin:
            logic_state[n] = 1
        elif logic_state[n-1] == 0 and U[n] >= Umax:
            logic_state[n] = 1
        elif logic_state[n-1] == 1 and U[n] <= Umin:
            logic_state[n] = 0
        else:
            logic_state[n] = logic_state[n-1]

        if logic_state_distorted[n-1] == 0 and U_distorted[n] < Umax:
            logic_state_distorted[n] = 0
        elif logic_state_distorted[n-1] == 1 and U_distorted[n] > Umin:
            logic_state_distorted[n] = 1
        elif logic_state_distorted[n-1] == 0 and U_distorted[n] >= Umax:
            logic_state_distorted[n] = 1
        elif logic_state_distorted[n-1] == 1 and U_distorted[n] <= Umin:
            logic_state_distorted[n] = 0
        else:
            logic_state_distorted[n] = logic_state_distorted[n-1]


    return U, U_distorted, logic_state * 4.5, logic_state_distorted * 4.5

ts = 1e-6  # Шаг по времени
time_end = 1e-3  # Общее время 

frequencies = [5e3, 10e3]  # Частоты в гц
T_values = [1e-5, 2e-5]  # Постоянные времени T
A_values = [0.1, 0.3]  # Амплитуды помех
Umin, Umax = 1.5, 3.5  # Границы запрещенной зоны

# Визуализация
plt.figure(figsize=(15, 10))

for i, freq in enumerate(frequencies):
    for j, T in enumerate(T_values):
        signal = generate_signal(freq, time_end, ts)
        U, U_d, logic_output, lo2 = simulate_cascade(signal, T, A_values[j], Umin, Umax, ts)
        
        plt.subplot(len(frequencies), len(T_values), i*len(T_values) + j + 1)
        plt.plot(np.arange(0, time_end, ts), signal, label='Input Signal')
        plt.plot(np.arange(0, time_end, ts), U, label='Voltage with Capacitance')
        plt.plot(np.arange(0, time_end, ts), U_d, label='Distorted')
        plt.plot(np.arange(0, time_end, ts), logic_output, label='Logic Cascade Output', linestyle='--')
        plt.plot(np.arange(0, time_end, ts), lo2, label='Logic Cascade Output 2', linestyle='--')
        plt.title(f'Frequency: {freq/1e3}kHz, T: {T}, A: {A_values[j]}')
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.legend()

plt.tight_layout()
plt.show()
