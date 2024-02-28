let tasks = [];

function renderTasks() {
    const tasksElement = document.getElementById('tasks');
    tasksElement.innerHTML = '';
    tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.textContent = task.name;
        if (task.completed) {
            li.classList.add('completed');
        }
        const button = document.createElement('button');
        button.textContent = 'Delete';
        button.onclick = () => deleteTask(index);
        li.appendChild(button);
        li.onclick = () => toggleTask(index);
        tasksElement.appendChild(li);
    });
}

function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskName = taskInput.value.trim();
    if (taskName !== '') {
        tasks.push({ name: taskName, completed: false });
        renderTasks();
        taskInput.value = '';
    }
}

function toggleTask(index) {
    tasks[index].completed = !tasks[index].completed;
    renderTasks();
}

function deleteTask(index) {
    tasks.splice(index, 1);
    renderTasks();
}

renderTasks();
