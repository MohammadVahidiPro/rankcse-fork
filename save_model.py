import os
import torch


def save_model(args, model, optimizer, optimizer_head, current_epoch, path, id, best=False, conf=False):
    if conf and best:
        best_path = path / "best_model_confidence_avg.tar"
        # out = os.path.join(args.model_path, "checkpoint_{}.tar".format(current_epoch))
        state = {'net': model.state_dict(), 'optimizer': optimizer.state_dict(), 'optimizer_head': optimizer_head.state_dict(), 'epoch': current_epoch}
        torch.save(obj=state, f=best_path)
        return

    check_path = path / f"checkpoint_{current_epoch}.tar"
    # out = os.path.join(args.model_path, "checkpoint_{}.tar".format(current_epoch))
    state = {'net': model.state_dict(), 'optimizer': optimizer.state_dict(), 'optimizer_head': optimizer_head.state_dict(), 'epoch': current_epoch}
    torch.save(obj=state, f=check_path)

    if best:
        best_path = path / "best_model_avg.tar"
        # out = os.path.join(args.model_path, "checkpoint_{}.tar".format(current_epoch))
        state = {'net': model.state_dict(), 'optimizer': optimizer.state_dict(), 'optimizer_head': optimizer_head.state_dict(), 'epoch': current_epoch}
        torch.save(obj=state, f=best_path)

   

def save_model_10(args, model, optimizer, optimizer_head, current_epoch, path, id):
    check_path = path / f"last_10_epoch.tar"
    print(f"saving model at epoch {current_epoch}")
    # out = os.path.join(args.model_path, "checkpoi
    # nt_{}.tar".format(current_epoch))
    state = {'net': model.state_dict(), 'optimizer': optimizer.state_dict(), 'optimizer_head': optimizer_head.state_dict(), 'epoch': current_epoch}
    torch.save(obj=state, f=check_path)


def save_just_model(model):
    path = "last_model_rankcse_trainer_ease_diff.tar"
        # out = os.path.join(args.model_path, "checkpoint_{}.tar".format(current_epoch))
    state = {'net': model.state_dict()} #, 'optimizer': optimizer.state_dict(), 'optimizer_head': optimizer_head.state_dict(), 'epoch': current_epoch}
    torch.save(obj=state, f=path)
    return path